import requests

def get_summary(book, chapter):
    base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'
    # TODO: Create a URL string that will access the API for the given book and chapter
    # HINT: The URL should be in the format f"{base_url}{book.lower()}/{chapter}"
    formatted_book = book.lower().replace(" ", "")
    
    url = f"{base_url}{formatted_book}/{chapter}"
    try:
        response = requests.get(url)
        # Check for error (404 Not Found)
        if response.status_code != 200:
            return "Error: Chapter not found (Check your spelling or chapter number)."
            
        data = response.json()
        
        # Access 'chapter', then get the 'summary' key
        summary_text = data['chapter']['summary']
        return summary_text
        
    except KeyError:
        return "No summary available for this chapter."
    except Exception as e:
        return f"An error occurred: {e}"

    # HINT: Use the requests.get() method to access the API and return the JSON data
    # HINT: Extract the summary from the JSON data and return it


def run_summary_tool():

    # Print a welcome message as shown in the example. "Welcome to the Book of Mormon Summary Tool!"
    print("Welcome to the Book of Mormon Summary Tool!")
    while True:
        try:
            book = input("Which book of the Book of Mormon would you like? (e.g., 1 Nephi, Alma): ")
            chapter = input(f"Which chapter of {book} are you interested in? ")
            summary = get_summary(book, chapter)
            print(f"Summary of {book} Chapter {chapter}:\n{summary}\n")
        except KeyError:
            print("Invalid book or chapter or API structure changed. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        another = input("Would you like to view another (Y/N)?: ").strip().lower()
        if another != 'y':
            print("Thank you for using Book of Mormon Summary Tool!")
            break
    # Use a while loop to allow the user to input a book and chapter
    # Ask the user for the book and chapter they would like to view a summary of
    # Use the get_summary() function to retrieve the summary and print it
    # If the book or chapter is invalid, catch the KeyError and print an error message
    # Ask the user if they would like to view another summary
    # If the user does not want to view another summary, print "Thank you for using Book of Mormon Summary Tool!"
    # do not forget to finish or break the loop


if __name__ == "__main__":
    run_summary_tool()