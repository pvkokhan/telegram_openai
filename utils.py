import openai

def generate_response(prompt):
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completions.choices[0].text
    return response

def start(message):
    bot.send_message(message.chat.id, config.start_msg)

def lalala(message):
    global counter

    now = datetime.datetime.now()
    date_time = now.strftime(config.date_time_format)

    with open("log.txt", "a") as f:
        f.write(
            f"\n\n{counter} request start \n{date_time} \nUser {message.from_user.username}: \n {config.separator} \n{message.text}\n {config.separator} \n\n")

    user_input = message.text
    response = generate_response(user_input)
    bot.send_message(message.chat.id, response)
    with open("log.txt", "a") as f:
        f.write(f"bot:\n {config.separator} \n {response} \n {config.separator} \n{counter} request end")
    counter += 1


def get_counter():
    global counter

    with open("log.txt", "r") as f:
        lines = f.readlines()
        if lines == []:
            counter = 1
        else:
            last_line = lines[-1]
            counter_str = last_line.split(" ")[0]
            if counter_str == "":
                counter = 1
            else:
                counter = int(counter_str) + 1