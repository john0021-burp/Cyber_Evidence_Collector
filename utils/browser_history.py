import os
import sys
import shutil
import sqlite3
from datetime import datetime, timedelta

def get_history_path(browser):
    user_profile = os.environ.get("USERPROFILE") or os.environ.get("HOME")
    if browser == "Chrome":
        return os.path.join(user_profile, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "History")
    elif browser == "Edge":
        return os.path.join(user_profile, "AppData", "Local", "Microsoft", "Edge", "User Data", "Default", "History")
    elif browser == "Brave":
        return os.path.join(user_profile, "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Default", "History")
    elif browser == "Firefox":
        profiles_path = os.path.join(user_profile, "AppData", "Roaming", "Mozilla", "Firefox", "Profiles")
        if os.path.exists(profiles_path):
            for profile in os.listdir(profiles_path):
                places_path = os.path.join(profiles_path, profile, "places.sqlite")
                if os.path.exists(places_path):
                    return places_path
    elif browser == "Safari":
        if sys.platform == "darwin":
            return os.path.join(user_profile, "Library", "Safari", "History.db")
    return None

def parse_history(db_path, browser_name):
    if not os.path.exists(db_path):
        return {"error": f"{browser_name} history file not found."}

    temp_copy = f"temp_{browser_name.lower()}_history"
    shutil.copy2(db_path, temp_copy)

    history = []
    try:
        conn = sqlite3.connect(temp_copy)
        cursor = conn.cursor()

        if browser_name == "Firefox":
            cursor.execute("SELECT url, title, visit_count, last_visit_date FROM moz_places ORDER BY last_visit_date DESC LIMIT 50")
            rows = cursor.fetchall()
            for url, title, visit_count, last_visit_date in rows:
                if last_visit_date:
                    visit_time = datetime(1970, 1, 1) + timedelta(microseconds=last_visit_date)
                    visit_time_str = visit_time.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    visit_time_str = "N/A"
                history.append({
                    "url": url,
                    "title": title,
                    "visit_count": visit_count,
                    "last_visit_time": visit_time_str
                })

        elif browser_name == "Safari":
            cursor.execute("""SELECT
                                history_items.url,
                                history_items.title,
                                history_visits.visit_time,
                                history_visits.visit_count
                              FROM history_items
                              JOIN history_visits
                              ON history_items.id = history_visits.history_item
                              ORDER BY history_visits.visit_time DESC
                              LIMIT 50""")
            rows = cursor.fetchall()
            for url, title, visit_time, visit_count in rows:
                try:
                    visit_time_dt = datetime(2001, 1, 1) + timedelta(seconds=visit_time)
                    visit_time_str = visit_time_dt.strftime("%Y-%m-%d %H:%M:%S")
                except:
                    visit_time_str = "N/A"
                history.append({
                    "url": url,
                    "title": title,
                    "visit_count": visit_count,
                    "last_visit_time": visit_time_str
                })

        else:
            cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 50")
            rows = cursor.fetchall()
            for url, title, visit_count, last_visit_time in rows:
                visit_time = datetime(1601, 1, 1) + timedelta(microseconds=last_visit_time)
                history.append({
                    "url": url,
                    "title": title,
                    "visit_count": visit_count,
                    "last_visit_time": visit_time.strftime("%Y-%m-%d %H:%M:%S")
                })

        conn.close()
    finally:
        os.remove(temp_copy)

    return history

def collect_all_browser_histories():
    results = {}
    for browser in ["Chrome", "Edge", "Brave", "Firefox", "Safari"]:
        db_path = get_history_path(browser)
        if db_path:
            results[browser] = parse_history(db_path, browser)
        else:
            results[browser] = {"error": f"{browser} history file not found or not supported on this OS."}
    return results
