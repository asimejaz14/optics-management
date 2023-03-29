from django.core.management import BaseCommand
import random

from faker import Faker


class Command(BaseCommand):
    help = "Data Migrations For Users Service"

    def handle(self, *args, **kwargs):

        TABLE_NAME = "ORDER"
        fake = Faker()

        lens = ['blue cut', 'photo sun', 'transition', 'green shade', 'normal']
        frame = ['metal black frame', 'silver', 'plastic black', 'silver metal', 'brown']
        cost = [5000, 10000, 2000, 3500, 7200, 8400, 6300, 1500, 6000]


        from order.models import Order

        for i in range(0, 500):
            data_dict = {
                "customer_name": fake.name(),
                "customer_contact": "+923" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
                    random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
                    random.randint(0, 9)) + str(
                    random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)),
                "customer_dob": fake.date_of_birth(),
                "lens": random.choice(lens),
                "total_cost": random.choice(cost),
                "frame": random.choice(frame),
                "r_sph": str(round(random.uniform(-5.0, +5.0), 2)),
                "r_cyl": str(round(random.uniform(-5.0, +5.0), 2)),
                "r_axis": str(random.randint(0, 70)),
                "l_sph": str(round(random.uniform(-5.0, +5.0), 2)),
                "l_cyl": str(round(random.uniform(-5.0, +5.0), 2)),
                "l_axis": str(random.randint(0, 70)),
                "order_status": random.randint(0, 3),
                "delivery_datetime": fake.date_time(),
            }
            Order.objects.create(**data_dict)
            self.stdout.write(
                self.style.SUCCESS(f"{data_dict}")
            )

        self.stdout.write(
            self.style.SUCCESS(f"Data migrations for '{TABLE_NAME}' ran successfully!")
        )

