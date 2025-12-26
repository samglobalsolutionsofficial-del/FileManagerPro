
print('\n\t<<<<<...File Manager...>>>>>')
print('\t----------------------------\n')


import os
import shutil

# main folder name
folder_name = input('Enter the folder name: ')

# Func to show files and folders
def list_files(folder_name):
    global index
    try:
        file_filter = input('List (all/specific/search) files: ').lower().strip()

        # show all files and folders
        if file_filter in ['all-files' , 'all' , 'all-file']:
            print('\n')
            for index , all_files in enumerate(os.listdir(folder_name) , start=1):
                print(f'{index}. {all_files}')
            else:
                print(f'\nTotal Number of files and folders: {index}')


        # show specific files and folders with the help of extension
        elif file_filter in ['specific-file' , 'specific-files' , 'specific']:
            file_extension = input('Enter the specific file extension: ')
            print(f'\t\tList of all {file_extension} files\n')
            print('\n')
            file_num = 0
            for all_files in os.listdir(folder_name):
                if all_files.endswith(file_extension):
                    print(f'{all_files}')
                    file_num += 1
            print(f'\nTotal Number of {file_extension} files: {file_num}')


        # search file and folder
        elif file_filter in ['search' , 'find' , 'check']:
            search_file_name = input('Enter the file name to search: ')
            print('\n')
            if search_file_name in os.listdir(folder_name):
                print(f'File exist: {search_file_name}')
            else:
                print(f'File {search_file_name} don\'t exist in {folder_name}')

        else:
            print(f'Invalid Input!\nEnter Commands:\n\tall ---> To show all the files and folders')
            print(f'\tspecific ---> To show specific files with extension')
            print(f'\tsearch ---> To check the file exist or not')

    # handle exceptions/errors
    except ValueError as error1:
        print(f'Error: {str(error1)}')
    except Exception as error:
        print(f'Error: {str(error)}')


# Func to rename files and folders
def rename_files(folder_name):
    try:
        user = input('Rename (single/multiple) files: ').lower().strip()

        # rename single file and folders
        if user in ['single' , 's' , 'one' , 'one-file' , 'single-file']:
            old_name_input = input('Old file name with extension to rename: ')
            new_rename_input = input('New file name withe extension to rename: ')
            old_name = f'{folder_name}/{old_name_input}'
            new_name = f'{folder_name}/{new_rename_input}'
            os.rename(old_name , new_name)
            print('\n')
            print(f'Renamed {old_name_input} --> {new_rename_input}')

        # rename multiple files and folders
        elif user in ['multiple' , 'm' , 'multiple' , 'multiple-files']:
            new_files_name = input('Enter the new files name without extension: ')
            extension = input('Extension of file: ')
            for index , file_name in enumerate(os.listdir(folder_name) , start=1):
                print('\n')
                if file_name.endswith(extension):
                    old_path = f'{folder_name}/{file_name}'
                    new_name = f'{index}-{new_files_name}{extension}'
                    new_path = f'{folder_name}/{new_name}'
                    os.rename(old_path , new_path)
                    print(f'Renamed {file_name} --> {new_name}')

        else:
            print(f'Invalid Input!\nEnter Commands:\n\t\tsingle ---> To rename one file\n\t\tmultiple ---> To rename multiple files')

    # Handle exception and errors of rename function
    except ValueError as error2:
        print(f'Error: {str(error2)}')
    except Exception as error:
        print(f'Error: {str(error)}')


# Func to move the files and folders
def move_files(folder_name):
    try:
        user = input('Move (single/multiple) files: ').lower().strip()

        # move single file
        if user in ['single', 's', 'move single', 'single file', 'move single file']:
            source_file_name = input('Enter the name of file to move (source path): ')
            destination_folder_name = input('Enter the name of folder to move (destination path): ')
            source_path = os.path.join(folder_name, source_file_name)
            destination_folder_path = os.path.join(folder_name, destination_folder_name)

            # create folder if folder don't exist
            if not os.path.exists(destination_folder_path):
                print(f"Destination folder '{destination_folder_name}' doesn't exist\nCreating it...")
                os.makedirs(destination_folder_path)
            destination_path = os.path.join(destination_folder_path, source_file_name)
            try:
                shutil.move(source_path, destination_path)
                print('\n')
                print(f"Moved: {source_file_name} --> {destination_folder_name}/")
            except Exception as e:
                print(f"Error: {e}")

        # move multiple files
        elif user in ['multiple', 'm', 'move multiple', 'multiple file', 'move multiple file']:
            extension = input('Enter the extension of files to move: ')
            destination_folder_name = input('Enter the folder name to move (destination path): ')

            # list all the files and folders of folder_name
            print('\n')
            for files in os.listdir(folder_name):
                # list specific files with the help of extension
                if files.endswith(extension):
                    source_path = os.path.join(folder_name, files)
                    destination_folder_path = os.path.join(folder_name, destination_folder_name)
                    # create the folder if the folder don't exist
                    if not os.path.exists(destination_folder_path):
                        print(f"Destination folder '{destination_folder_name}' doesn't exist.\nCreating it...")
                        os.makedirs(destination_folder_path)
                    destination_path = os.path.join(destination_folder_path, files)
                    try:
                        shutil.move(source_path, destination_path)
                        print(f"Moved: {extension} --> {destination_folder_name}/")
                    except Exception as e:
                        print(f"Error: {e}")
        else:
            print('Invalid Input!\nEnter Commands:\n\t\tsingle ---> To move single file\n\t\tmultiple ---> To move multiple files')
            # handle exception and errors
    except Exception as error:
        print(f'Error: {str(error)}')


# Func to copy the files and folders
def copy_files(folder_name):
    try:
        files_folders = input('Copy (file/folder): ').lower().strip()

        # copy the files only
        if files_folders in ['file' , 'files' , 'copy file' , 'copy files']:
            user = input('Copy (single/multiple) file: ').lower().strip()

            # copy single files
            if user in ['single', 's', 'copy single', 'single file', 'copy single file']:
                source_file_name = input('Enter the file name to copy (source path): ')
                destination_folder_name = input('Enter the folder name to copy (destination path): ')
                source_path = os.path.join(folder_name, source_file_name)
                destination_folder_path = os.path.join(folder_name, destination_folder_name)

                # if the folder don't exist then create it
                if not os.path.exists(destination_folder_path):
                    print(f"Destination folder '{destination_folder_name}' doesn't exist.\nCreating it...")
                    os.makedirs(destination_folder_path)
                destination_path = os.path.join(destination_folder_path, source_file_name)
                try:
                    shutil.copy(source_path, destination_path)
                    print('\n')
                    print(f"Copy: {source_file_name} --> {destination_folder_name}/")
                except Exception as e:
                    print(f"Error: {e}")

            # copy multiple files
            elif user in ['multiple', 'm', 'copy-multiple', 'multiple-file', 'move-copy-file']:
                extension = input('Enter the extension of files to copy (source path): ')
                destination_folder_name = input('Enter the folder name to copy (destination path): ')

                # list all the files and folders of folder_name
                for files in os.listdir(folder_name):
                    # list of specific files with the help of extension
                    if files.endswith(extension):
                        source_path = os.path.join(folder_name, files)
                        destination_folder_path = os.path.join(folder_name, destination_folder_name)

                        # if the folder don't exist then create it
                        if not os.path.exists(destination_folder_path):
                            print(f"Destination folder '{destination_folder_name}' doesn't exist.\nCreating it...")
                            os.makedirs(destination_folder_path)
                        destination_path = os.path.join(destination_folder_path, files)
                        try:
                            shutil.copy(source_path, destination_path)
                            print('\n')
                            print(f"Copy: {extension} --> {destination_folder_name}/")
                        except Exception as e:
                            print(f"Error: {e}")
            else:
                print('Invalid Input!\nEnter Commands:\n\t\tsingle ---> To copy single files\n\t\tmultiple ---> To copy multiple files')

        # copy folder only
        elif files_folders in ['folder' , 'folders' , 'copy folders' , 'copy folder']:
            if files_folders in ['folder', 'folders', 'copy folder', 'copy folder']:
                user1 = input('Copy (single/multiple) folder: ').lower().strip()

                # copy single folder
                if user1 in ['single', 's', 'copy single', 'single folder', 'copy single folder']:
                    source_file_name = input('Enter the folder name to copy (source path): ')
                    destination_folder_name = input('Enter the folder name to copy (destination path): ')
                    source_path = os.path.join(folder_name, source_file_name)
                    destination_folder_path = os.path.join(folder_name, destination_folder_name)

                    # if the folder don't exist then create it
                    if not os.path.exists(destination_folder_path):
                        print(f"Destination folder '{destination_folder_name}' doesn't exist.\nCreating it...")
                        os.makedirs(destination_folder_path)
                    destination_path = os.path.join(destination_folder_path, source_file_name)
                    try:
                        shutil.copytree(source_path, destination_path)
                        print('\n')
                        print(f"Copy: {source_file_name} --> {destination_folder_name}/")
                    except Exception as e:
                        print(f"Error: {e}")

                # copy multiple folders
                elif user1 in ['multiple', 'm', 'copy multiple', 'multiple folder', 'move copy folder']:
                    extension = input('Enter the extension of files to copy (source path): ')
                    destination_folder_name = input('Enter the folder name to copy (destination path): ')

                    # list all the files and folders of folder_name
                    for files in os.listdir(folder_name):
                        # list of specific files with the help of extension
                        if files.endswith(extension):
                            source_path = os.path.join(folder_name, files)
                            destination_folder_path = os.path.join(folder_name, destination_folder_name)

                            # if the folder don't exist then create it
                            if not os.path.exists(destination_folder_path):
                                print(f"Destination folder '{destination_folder_name}' doesn't exist.\nCreating it...")
                                os.makedirs(destination_folder_path)
                            destination_path = os.path.join(destination_folder_path, files)
                            try:
                                shutil.copytree(source_path, destination_path)
                                print('\n')
                                print(f"Copy: {extension} --> {destination_folder_name}/")
                            except Exception as e:
                                print(f"Error: {e}")
                else:
                    print(
                        'Invalid Input!\nEnter Commands:\n\t\tsingle ---> To copy single folder\n\t\tmultiple ---> To copy multiple folder')

    except Exception as error:
        print(f'Error: {error}')


# Func to delete files and folders
def delete_files(folder_name):
    try:
        user = input('Delete (folder/file): ').lower().strip()

        # Delete folders
        if user in ['folder' , 'folders' , 'directory']:
            delete_single_multiple_folder = input('Delete (single/multiple) folder: ').lower().strip()

            # Delete single folder
            if delete_single_multiple_folder in ['single' , 'single folder']:
                delete_folder = input('Delete (empty/not empty) single folder: ').lower().strip()

                # delete single empty folder
                if delete_folder in ['empty' , 'empty folder']:
                    empty_folder_name = input('Enter the empty folder name to delete: ')
                    empty_folder_path = os.path.join(folder_name,empty_folder_name)
                    os.rmdir(empty_folder_path)
                    print('\n')
                    print(f'Delete empty folder: {empty_folder_path}')

                # delete single not empty folder
                elif delete_folder in ['not empty' , 'not empty folder']:
                    not_empty_folder_name = input('Enter the not empty folder name to delete: ')
                    not_empty_folder_path = os.path.join(folder_name , not_empty_folder_name)
                    shutil.rmtree(not_empty_folder_path)
                    print('\n')
                    print(f'Delete not empty folder: {not_empty_folder_path}')

                else:
                    print('\n')
                    print('Invalid Input!\nEnter Commands:\n\t\tempty ---> To delete empty single folder')
                    print('\t\tnot empty ---> To delete not empty single folder')

            # Delete multiple folders
            elif delete_single_multiple_folder in ['multiple' , 'multiple folder']:
                delete_folder_multiple = input('Delete (empty/not empty) multiple folders: ').lower().strip()

                # Delete all empty folders
                if delete_folder_multiple in ['empty', 'empty folder']:
                    folder_endswith = input('Enter the same extension of empty folders to delete: ')
                    print('\n')
                    for folder in os.listdir(folder_name):
                        if folder.endswith(folder_endswith):
                            os.rmdir(f'{folder_name}/{folder}')
                            print(f'Delete all empty folders: {folder}')

                # Delete all not empty folders
                elif delete_folder_multiple in ['not empty', 'not empty folder']:
                    multiple_folder_endswith = input('Enter the same extension of not empty folders to delete: ')
                    print('\n')
                    for multiple_folder in os.listdir(folder_name):
                        if multiple_folder.endswith(multiple_folder_endswith):
                            shutil.rmtree(f'{folder_name}/{multiple_folder}')
                            print(f'Delete all not empty folders: {multiple_folder}')
                else:
                    print('\n')
                    print('Invalid Input!\nEnter Commands:\n\t\tempty ---> To delete multiple empty folders')
                    print(f'\t\tnot empty ---> To delete multiple not empty folders')
            else:
                print('\n')
                print(f'Invalid Input!\n\t\tEnter Commands:\n\t\tsingle ---> To delete single folder')
                print(f'\t\tmultiple ---> To delete multiple folders')

        # Delete files
        elif user in ['file' , 'files' ]:
            if user in ['file', 'files']:
                single_or_multiple_files = input('Delete (single/multiple) file: ').lower().strip()

                # Delete single file
                if single_or_multiple_files in ['single', 'single file']:
                    single_file_name = input('Enter the single file name to delete: ')
                    single_file_path = os.path.join(folder_name, single_file_name)
                    os.remove(single_file_path)
                    print('\n')
                    print(f'Delete single file: {single_file_path}')

                # Delete multiple files
                elif single_or_multiple_files in ['multiple', 'multiple file']:
                    multiple_file_name = input('Enter the same extension of files to delete: ')
                    print('\n')
                    for files_extension in os.listdir(folder_name):
                        if files_extension.endswith(multiple_file_name):
                            multiple_file_path = os.path.join(folder_name, files_extension)
                            os.remove(multiple_file_path)
                            print(f'Delete all multiple files: {multiple_file_path}')
                    else:
                        print('Files don\'t exist!')

                else:
                    print('\n')
                    print('Invalid Input!\nEnter Commands:\n\t\tsingle ---> To delete single file')
                    print('\t\tmultiple ---> To delete multiple files')

        else:
            print('\n')
            print('Invalid Input!\nEnter Commands:\n\t\tfile ---> To delete files\n\t\tfolder ---> To delete folders')

    # handle error and exceptions
    except Exception as error:
        print(f'Error: {str(error)}')


# Func to create files and folders
def create_files(folder_name):
    try:
        user = input('Create (file/folder): ').lower().strip()

        # Create files
        if user in ['file' , 'files' , 'create files']:
            user_files = input('Create (single/multiple) files: ')

            # Create single file
            if user_files in ['single' , 'single file' , 'single files']:
                file_name = input('Enter the name of file to create without extension: ')
                file_extension = input('Enter the file extension to create file: ')
                print('\n')
                with open(f'{folder_name}/{file_name}{file_extension}' , 'x'):
                    print(f'Single file is Created: {file_name}{file_extension}')


            # Create multiple files
            elif user_files in ['multiple' , 'multiple file' , 'multiple files']:
                multiple_file_name = input('Enter the name of multiple files without extension: ')
                multiple_file_extension = input('Enter the file extension: ')
                number_of_files = int(input('How many files do you want to create: '))
                print('\n')
                for number in range(1, number_of_files + 1):
                    with open(f'{folder_name}/{number}-{multiple_file_name}{multiple_file_extension}' , 'x'):
                        print(f'Multiple files are Created: {folder_name}/{number}{multiple_file_name}{multiple_file_extension}')
            else:
                print(f'Invalid Input!\nEnter Commands:\n\t\tsingle ---> To create single file')
                print(f'\t\tmultiple ---> To create multiple files')

        # Create folders
        elif user in ['folder' , 'folders' , 'create folders']:
            single_multiple_folder_name = input('Create (single/multiple) folder: ').lower().strip()

            # Create single folder
            if single_multiple_folder_name in ['single' , 'single folder']:
                single_folder_name = input('Enter the name of folder to create: ')
                os.mkdir(f'{folder_name}/{single_folder_name}')
                print('\n')
                print(f'Create single folder: {single_folder_name}')

                # Create single folder with single and multiple file
                folder_with_file = input('Do you want to create file in this folder(yes/no): ').lower().strip()
                if folder_with_file == 'yes':
                    single_multiple = input('Create (single/multiple) file: ').lower().strip()

                    # Create single file in single folder
                    if single_multiple == 'single':
                        file_name = input('Enter the name of file with extension: ')
                        print('\n')
                        with open(f'{folder_name}/{single_folder_name}/{file_name}' , 'x'):
                            print(f'Create {single_folder_name} folder with {file_name} file.')

                    # Create multiple files in single folder
                    elif single_multiple == 'multiple':
                        file_n = input('Enter the name of files with extension to create in folder: ')
                        no_of_files = int(input('How many files do you want to create: '))
                        print('\n')
                        for number in range(1 , no_of_files +1):
                            with open(f'{folder_name}/{single_folder_name}/{number}-{file_n}' , 'x'):
                                print(f'Files are created in {single_folder_name}')


            # Create multiple folders
            elif single_multiple_folder_name in ['multiple' , 'multiple folder']:
                multiple_folder_name = input('Enter multiple folders name: ')
                number_of_folders = int(input('How many folders do you want to create: '))


                # Var_ which ask the user to create only folders , folders with single or multiple files
                files_with_folders = input('Create (folders only/folders with single file/folders with multiple files): ').lower().strip()

                # Create only multiple folders
                if files_with_folders in ['folders' , 'folders only']:
                    print('\n')
                    for number in range(1, number_of_folders + 1):
                        multiple_folder_path = f'{folder_name}/{number}-{multiple_folder_name}/'
                        os.makedirs(multiple_folder_path)
                        print(f'Multiple Folders are Created! ---> {multiple_folder_path}')

                # Create single file in each folder
                elif files_with_folders in ['folders with single file']:
                    add_file_folder = input('Name with extension of file to create in each folder: ')  # add file in each folder
                    print('\n')
                    for number in range(1, number_of_folders + 1):
                        folder_path = f'{folder_name}/{number}-{multiple_folder_name}'
                        os.makedirs(folder_path)
                        folderpath_filepath = f'{folder_path}/{add_file_folder}'
                        with open(f'{folderpath_filepath}' , 'x'):
                            print(f'Create file in each folder! ---> {folderpath_filepath}')

                # Create multiple files in each folder
                elif files_with_folders in ['folders with multiple files']:
                    multiple_files_name = input('Name of multiple files with extension to create in each folder: ')
                    no_of_mul_files = int(input('How many files you create in each folder: '))
                    print('\n')
                    for folder_number in range(1 , number_of_folders + 1):
                        folder_path = f'{folder_name}/{folder_number}-{multiple_folder_name}'
                        os.makedirs(folder_path)
                        for file_number in range(1 , no_of_mul_files + 1):
                            folder_path_mul_files = f'{folder_path}/{file_number}-{multiple_files_name}'
                            with open(f'{folder_path_mul_files}' , 'x'):
                                print(f'Create multiple files in each folder! ---> {folder_path_mul_files}')
                else:
                    print('\n')
                    print(f'Invalid Input!\nEnter Commands:\n\t\tfolders only ---> To create only multiple folders')
                    print(f'\t\tfolders with single file ---> To create single file in each folder')
                    print(f'\t\tfolders with multiple file ---> To create multiple files in each folder')

            else:

                print(f'Invalid Input!\nEnter Commands:\n\t\tsingle ---> To create single folder')
                print(f'\t\tmultiple ---> To create multiple folders')

        else:
            print(f'Invalid Input!\nEnter Commands:\n\t\tfile ---> To create files')
            print(f'\t\tfolder ---> To create folders')

    # handle errors
    except Exception as error:
        print(f'Error: {str(error)}')


# Func to read the file
def read_file(folder_name):
    try:
        enter_file_name = input('Enter the file name to read: ').lower().strip()
        file_path = f'{folder_name}/{enter_file_name}'

        # open and read the file content 
        with open(file_path , 'r') as file:
            file_content = file.read()
            print(f'\n{file_content}')

    # handle the errors
    except FileNotFoundError as error1:
        print(f'Error: {str(error1)}')
    except Exception as error:
        print(f'Error: {str(error)}')


# Func to show the details of files
def detail_files(folder_name):
    try:
        file_name = input('Enter the file name :')
        file_path = f'{folder_name}/{file_name}'

        # open and read all the file
        with open(file_path , 'r') as file:
            content = file.read()
            characters = len(content)     # show all the number characters
            lines = content.splitlines()  # show all number of lines
            words = content.split()       # show all the number of words

            print(f'\n\t\tDetail of {file_name} file')
            print(f'File name: {file_name}')
            print(f'Total number of characters: {characters}')
            print(f'Total number of lines: {len(lines)}')
            print(f'Total number of words: {len(words)}')

    # handle the exception errors
    except Exception as error:
        print(f'Error: {str(error)}')


# Func to convert one file to another file
def convert_files(folder_name):
    print('\nIMPORTANT NOTE:\n\t\tFile Conversion will remove your existing data')
    user_input = input('Conversion (single/multiple) files: ').lower().strip()

    # Convert single file form one type to another type
    if user_input in ['single' , 'single file']:
        old_file_name = input('Enter old file name with extension to convert: ')
        new_file_name = input('Enter new file name with extension to convert: ')
        old_path = f'{folder_name}/{old_file_name}'
        new_path = f'{folder_name}/{new_file_name}'

        os.rename(old_path , new_path)
        print('\n')
        print(f'Convert file:\n\t\t{old_file_name} ---> {new_file_name}')

    # Convert multiple files from one type to another type
    elif user_input in ['multiple' , 'multiple file' , 'multiple files']:
        new_files_name = input('Enter the new files name without extension: ')
        old_extension = input('Enter old extension of file: ')
        new_extension = input('Enter new extension of file: ')

        print('\n')
        for index, file_name in enumerate(os.listdir(folder_name), start=1):
            if file_name.endswith(old_extension):
                old_path = f'{folder_name}/{file_name}'
                new_name = f'{index}-{new_files_name}{new_extension}'
                new_path = f'{folder_name}/{new_name}'
                os.rename(old_path, new_path)
                print(f'Convert file: {file_name} --> {new_name}')
    else:
        print("Invalid Input!")
        print(f'Enter Commands:\n\t\tsingle ---> To convert single file')
        print(f'\t\tmultiple ---> To convert multiple files')


# Repeat the program
while True:
    user = input('What do you want to do: ').lower().strip()

    # Show results on the basics of Conditional Statements
    if user in ['list file' , 'lists' , 'list files' , 'list']:
        list_files(folder_name)
    elif user in ['rename file' , 'rename' , 'renames' , 'rename files']:
        rename_files(folder_name)
    elif user in ['move file' , 'move' , 'moves' , 'move files']:
        move_files(folder_name)
    elif user in ['copy file' , 'copy' , 'copy files']:
        copy_files(folder_name)
    elif user in ['delete file' , 'delete' , 'deletes' , 'delete files']:
        delete_files(folder_name)
    elif user in ['create file' , 'create' , 'create files']:
        create_files(folder_name)
    elif user in ['read file' , 'read' , 'read files']:
        read_file(folder_name)
    elif user in ['detail file' , 'detail' , 'detail files']:
        detail_files(folder_name)
    elif user in ['convert file' , 'convert' , 'converter']:
        convert_files(folder_name)
    elif user in ['exit' , 'stop' , 'quite']:
        print('Exit the program!')
        break

    else:
        print('\n')
        print(f'Invalid Input!\nEnter Commands:')
        print(f'\t\tlist    ---> To list all the file and folder.')
        print(f'\t\trename  ---> To rename file and folder.')
        print(f'\t\tmove    ---> To move file and folder.')
        print(f'\t\tcopy    ---> To copy file and folder.')
        print(f'\t\tdelete  ---> To delete file and folder.')
        print(f'\t\tcreate  ---> To create file and folder.')
        print(f'\t\tread    ---> To read file and folder.')
        print(f'\t\tdetail  ---> To detail file and folder.')
        print(f'\t\tconvert ---> To convert file and folder.')
        print(f'\t\texit    ---> To exit file and folder.')
    print('\n')

