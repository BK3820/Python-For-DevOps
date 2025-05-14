import os

def filelist(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "Provide a valid folder path."
    except Exception as e:
        return None, str(e)

def main():
    # Accepting multiple folder paths separated by spaces
    folders = input("Provide the folder paths (separated by spaces): ").split()
    
    for folder in folders:
        print(f"\nFolder path: {folder}")
        files, error = filelist(folder)

        if files:
            print("Files in the folder:")
            for file in files:
                print(file)
        else:
            print("Error:", error)

if __name__ == "__main__":
    main()
