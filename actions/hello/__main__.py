def main(args):
    name = args.get("name", "stranger")  
    greeting = "Haaaaallo " + name + "!"
    print(greeting)
    return {"greeting": greeting}

# for local testing
if __name__ == "__main__": 
    main({})