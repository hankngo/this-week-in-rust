class Event:
    def __init__(self, name, location, date, url, virtual, organizer_name, organizer_url):
        """
        Initialize an Event object.

        Args:
            name (str): The name of the event.
            location (str): The location of the event.
            date (datetime.date): The date of the event.
            url (str): The URL for more details about the event.
            virtual (bool): Whether the event is virtual.
            organizer_name (str): The name of the event organizer.
            organizer_url (str): The URL of the organizer's profile or website.
        """
        self.name = name
        self.location = location
        self.date = date
        self.url = url
        self.virtual = virtual
        self.organizer_name = organizer_name
        self.organizer_url = organizer_url

    def __repr__(self):
        """
        Provide a string representation of the Event object for debugging.
        """
        return (
            f"Event(name={self.name!r}, location={self.location!r}, date={self.date!r}, "
            f"url={self.url!r}, virtual={self.virtual!r}, "
            f"organizer_name={self.organizer_name!r}, organizer_url={self.organizer_url!r})"
        )
