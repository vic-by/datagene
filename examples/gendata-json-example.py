from Mixer import Mixer, get_from_list, shuffled_ints, shuffled_decs

if __name__ == "__main__":
    fn = get_from_list("../lists/firstnames.txt")
    ln = get_from_list("../lists/lastnames.txt")
    dates_f = get_from_list("../lists/dates.txt")
    systems_f = get_from_list("../lists/systems.txt")
    device_agents_f = get_from_list("../lists/device_agents.txt")

    mixer = Mixer()
    mixer.set_delimiter('|')
    mixer.add_column(fn, name="first_name")
    mixer.add_column(ln, name="last_name")
    mixer.add_column(shuffled_ints(1, 5), name="shuffled_ints")
    mixer.add_column(systems_f, name="system")
    mixer.add_column(device_agents_f, name="device_agent")
    mixer.add_column(dates_f, name="date")
    print mixer.json(number_of_records=26)

    with open('sample-data.json', "w+") as f:
        f.writelines(mixer.json(number_of_records=100000))
