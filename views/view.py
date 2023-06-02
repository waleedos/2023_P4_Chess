from utils.check_date import check_date


class View:

    @staticmethod
    def get_user_entry(msg_display, msg_error, value_type, assertions=None, default_value=None):

        while True:

            value = input(msg_display)

            if value_type == "numeric":

                if value.isnumeric():

                    value = int(value)
                    return value

                else:
                    print(msg_error)

                    continue

            if value_type == "num_superior":

                if value.isnumeric():
                    value = int(value)
                    if value >= default_value:
                        return value
                    else:
                        print(msg_error)
                        continue
                else:
                    print(msg_error)
                    continue
            if value_type == "string":

                try:
                    float(value)
                    print(msg_error)
                    continue
                except ValueError:
                    return value

            elif value_type == "date":

                if check_date(value):
                    return value
                else:
                    print(msg_error)
                    continue

            elif value_type == "selection":

                if value in assertions:
                    return value
                else:
                    print(msg_error)
                    continue

    @staticmethod
    # décorateur qui indique que la méthode suivante est une méthode statique
    def build_selection(iterable, display_msg, assertions):

        display_msg = display_msg
        assertions = assertions
        for i, data in enumerate(iterable):
            display_msg = display_msg + f"{i + 1} - {data['name']}\n"
            assertions.append(str(i + 1))

        return {
            "msg": display_msg,
            "assertions": assertions
        }
