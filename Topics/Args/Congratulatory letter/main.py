def congratulations(pm, t, *devs):
    message = f"Happy New Year! Take care of yourself and your loved ones!\n" \
              f"For:\n" \
              f"{pm}\n" \
              f"{t}"
    for dev in devs:
        message = message + "\n" + dev
    # print(message)

    print(message)


# congratulations("Alice", "Mike", "Roman", "Victoria")
