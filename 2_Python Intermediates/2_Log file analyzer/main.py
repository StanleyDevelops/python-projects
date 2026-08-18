# File log analyzer

with open("server.log", "r") as file:

    print("================= LOG REPORT =================")
    frequency_dict = {}    # count all error types
    error_messages = []    # to collect error messages

    log_count = 0

    for line in file:
        parts = line.strip().split()   # 
        if not parts:      # to check if line is empty
            continue
        level = parts[0]               # extract the error type
        if level == "ERROR":
            message = error_messages.append(" ".join(parts[1:]))   # join the rest of message

        if level in frequency_dict:
            frequency_dict[level] += 1
        else:
            frequency_dict[level] = 1
                

        log_count += 1
   
    # print count of error type
    for key, value in frequency_dict.items():

        # find percentage of each error
        percentage = (value / log_count) * 100
        print(f"{key}: {value} ({float(percentage)}%)")

    print(f"{"-"*45}")

    print(f"Error Messages")
    for i, message in enumerate(error_messages, start = 1):
        print(f"{i}. {message}")

    print(f"{"-"*45}")

    # count Error mesages
    most_common_error = {}
    for message in error_messages:
        most_common_error[message] = most_common_error.get(message, 0) + 1

    # find most common error message
    most_common = max(most_common_error, key=most_common_error.get)
    print(f"Most Common Error:")
    print(f"{most_common} ({most_common_error[most_common]})")

    print(f"{"-"*45}")

    print(f"Total Log Entries: {log_count}")

    print(f"{"-"*45}")

   





    



    
