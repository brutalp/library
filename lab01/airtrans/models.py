from django.db import models


class Booking(models.Model):
    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateField()
    total_amount = models.FloatField(null=False)

    def __str__(self):
        return "{} - {}".format(self.book_ref, self.book_date)


class Ticket(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    book_ref = models.ForeignKey('Booking', on_delete=models.CASCADE)
    passenger_id = models.PositiveIntegerField(null=False)
    passenger_name = models.TextField(max_length=100)
    contact_data = models.TextField(max_length=200)

    def __str__(self):
        return "{} - {}".format(self.ticket_no, self.passenger_name)


class Ticket_flight(models.Model):
    ticket_no = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)
    fare_conditions = models.TextField()
    amount = models.IntegerField(null=False)

    def __str__(self):
        return "{} - {} - {}".format(self.ticket_no, self.flight_id, self.fare_conditions)


class Boarding_passes(models.Model):
    ticket_no = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)
    boarding_no = models.PositiveIntegerField(null=False)
    seat_no = models.TextField(max_length=10)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'), )

    def __str__(self):
        return "{} - {} - {}".format(self.ticket_no, self.flight_id, self.boarding_no)


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_no = models.TextField(max_length=10)
    scheduled_departure = models.TextField(max_length=100)
    scheduled_arrival = models.TextField(max_length=100)
    departure_airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='scheduled_departure')
    arrival_airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='scheduled_arrival')
    status = models.TextField(max_length=100)
    aircraft_code = models.TextField(max_length=100)
    actual_departure = models.TextField(max_length=100)
    actual_arrival = models.TextField(max_length=100)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.flight_id, self.flight_no, self.scheduled_departure, self.scheduled_arrival)


class Airport(models.Model):
    airport_code = models.CharField(max_length=10)
    airport_name = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    coordinates = models.CharField(max_length=100)
    timezone = models.CharField(max_length=15)

    def __str__(self):
        return "{} - {}".format(self.airport_code, self.airport_name)


class Aircraft(models.Model):
    aircraft_code = models.PositiveIntegerField(null=False)
    model = models.TextField(max_length=100)
    range = models.TextField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.aircraft_code, self.model)


class Seats(models.Model):
    aircraft_code = models.ForeignKey('Aircraft', on_delete=models.CASCADE)
    seat_no = models.TextField(max_length=10)
    fare_conditions = models.TextField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.aircraft_code, self.seat_no)
