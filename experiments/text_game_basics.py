import time, os

def dialogue(file, list_index_start = 0, list_index_end = "end", delay_1 = 0.05, delay_2 = 0.3,):
   
    """Hello"""

    try:
        with open(file) as file:
            file = file.read().splitlines()
            if list_index_end == "end":
                list_index_end = len(file)

            for x in file[list_index_start: list_index_end]:
                for y in x:
                    print(y, end = "", flush = True)
                    time.sleep(delay_1)
                time.sleep(delay_2)
                print("")

    except:
        if type(file) == list:
            for x in file:
                for y in x:
                    print(y, end = "", flush = True)
                    time.sleep(delay_1)
                time.sleep(delay_2)
                print("")

        else:
            for x in file:
                print(x, end = "", flush = True)
                time.sleep(delay_1)
            print("")
            time.sleep(delay_2)


def check_point(save_file_name, save_mode, check_point_name = ""):
    if save_mode == "w":
        try:
            with open(f"{save_file_name}", "x") as file:
                file.write(check_point_name)

        except:
            with open(f"{save_file_name}", "a") as file:
                file.write(check_point_name)

    elif save_mode == "r":

        try:
            with open(f"{save_file_name}", "r") as file:
                if check_point_name in file:
                    return True
        except:
            pass

    elif check_point_name == "d" or save_mode == "d":
        os.remove(f"{save_file_name}")
