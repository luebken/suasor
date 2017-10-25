def main(args):
    name = args.get("name", "stranger")  
    greeting = "Haaaaallo " + name + "!"
    print(greeting)
    return {"greeting": greeting}
