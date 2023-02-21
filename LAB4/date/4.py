from datetime import*
def date_diff_in_Seconds(today, yesterday):
    timedelta = today - yesterday
    return timedelta.days * 24 * 3600 + timedelta.seconds
delta = timedelta(1)
today1 = datetime.now()
yesterday1 = today1 - delta
print("\n%d seconds" %(date_diff_in_Seconds(today1, yesterday1)))
