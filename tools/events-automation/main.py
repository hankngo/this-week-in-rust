from generate_events_meetup import get_events

def main():
    events_list = get_events()
    for event in events_list:
        print(event, "\n\n")


if __name__ == "__main__":
    main()