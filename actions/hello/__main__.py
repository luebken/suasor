def main(args):
    name = args.get("name", "stranger")  
    greeting = "Haaaaallo " + name + "!"
    result = {"body": "<html><body><h3>"+greeting+"</h3></body></html>"}
    print(result)
    return result

# for local testing
if __name__ == "__main__": 
    main({})