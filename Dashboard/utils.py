from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event ,Intervention

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(Date__day=day)


		d = ''
		for event in events_per_day:
			d += f'<p> {event.get_html_url} </p>'

		if day != 0:
			if events_per_day.exists():
				return f"<td style='background-color:A8DF8E '><span class='date'>{day}</span><ul class='dateevent'> {d} </ul></td>"
			else:
				return f"<td><span class='date'>{day}</span><ul class='dateevent'> {d} </ul></td>"

		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Intervention.objects.filter(Date__year=self.year, Date__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
