import os
import csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_demo_2.settings")
import django
django.setup()
def main():
    from charts.models import Chart
    with open('test_data.csv','r') as f:
        ChartList = []
        f_csv = csv.reader(f)
        headers = next(f_csv)
        print(headers)
        for line in f_csv:
            print(line)
            # ChartList.append(Chart(time=line[0],predict=line[1]))
            # break
            Chart.objects.create(time=line[0],predict=line[1])
    # Chart.objects.bulk_create(ChartList)
if __name__ == "__main__":

    main()