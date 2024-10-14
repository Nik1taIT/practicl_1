total_seconds = 3 * 24 * 60 * 60
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"Hours:    {hours:<10}")
print(f"Minutes:  {minutes:<10}")
print(f"Seconds:  {seconds:<10}")