from dalga_app import DalgaApp

def main():
    app = DalgaApp()

    print("DALGA, Data Analysis LangGraph Agent")
    print("Type 'quit' to exit")


    while True:
        user_input = input("Question: ").strip()

        if user_input.lower() == 'quit':
            break

        try: 
            answer = app.forward(user_input)
            print(answer)

        except Exception as e:
            print(f"Error: {str(e)}")

    
if __name__ == "__main__":
    main()