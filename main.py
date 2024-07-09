def add_time(start, duration, day_of_week=False):
  days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
  days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  # Parsing duration time
  duration_tuple = duration.partition(":")
  duration_hours = int(duration_tuple[0])
  duration_minutes = int(duration_tuple[2])

  # Parsing start time
  start_tuple = start.partition(":")
  start_minutes_tuple = start_tuple[2].partition(" ")
  start_hours = int(start_tuple[0])
  start_minutes = int(start_minutes_tuple[0])
  am_or_pm = start_minutes_tuple[2]

  am_and_pm_flip = {"AM": "PM", "PM": "AM"}
  amount_of_days = duration_hours // 24

  # Calculate end time
  end_minutes = start_minutes + duration_minutes
  if end_minutes >= 60:
      start_hours += 1
      end_minutes = end_minutes % 60

  end_hours = (start_hours + duration_hours) % 12
  end_hours = 12 if end_hours == 0 else end_hours
  end_minutes = str(end_minutes).zfill(2)  # Ensure minutes are two digits

  total_hours = start_hours + duration_hours
  amount_of_am_pm_flips = (total_hours // 12)

  if am_or_pm == "PM" and (total_hours % 12) >= 12:
      amount_of_days += 1

  am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm

  return_time = f"{end_hours}:{end_minutes} {am_or_pm}"

  if day_of_week:
      day_of_week = day_of_week.lower()
      index = (days_of_the_week_index[day_of_week] + amount_of_days) % 7
      new_day = days_of_the_week_array[index]
      return_time += f", {new_day}"

  if amount_of_days == 1:
      return return_time + " (next day)"
  elif amount_of_days > 1:
      return return_time + f" ({amount_of_days} days later)"

  return return_time

# Test the function
print(add_time("11:06 PM", "2:02"))
print(add_time("8:16 PM", "3:02"))
print(add_time("11:59 PM", "24:05"))

