from collections import UserDict

class Field():
    pass

class Name():
    def add(self, user_name):
        self.value = user_name
    value = ''

class Phone():
    def add(self, user_phone):
        self.value = user_phone
    value = ''

class Record(Field, Name, Phone):
    phone_list = []
    def Add(self, user_name, user_phone):
        self.name = Name()
        self.name.add(user_name)
        if user_phone != '':
            self.phone_list.append(Phone())
            self.phone_list[0].add(user_phone)

    def Delete(self):
        self.phone_list.clear()

    def Edit(self, new_phone):
        self.phone_list[0].value = new_phone

class AddressBook(UserDict, Record):
    dict = {}

    def find_by_name(self, name):
        print(f'name: {name}')
        for phone in self.dict[name].phone_list:
            print(f'\t {phone.value}')

    def find_by_phone(self, phone):
        for key, value in self.dict.items():
            for phone_to_find in value.phone_list:
                if phone_to_find.value == phone:
                    print(f'{key}:{phone}')

    def add_record(self, user_name, user_phone=''):
        record = Record()
        record.Add(user_name, user_phone)
        self.dict.update({record.name.value: record})

    def process(self, list_of_commands):
        #print(f'process: {list_of_commands}')
        if len(list_of_commands) == 1:
            if list_of_commands[0] == 'hello':
                print('How can I help you?')
            elif list_of_commands[0] == 'close' or list_of_commands[0] == 'exit':
                print('Good bye!')
                exit()
        elif len(list_of_commands) == 2:
            if list_of_commands[0] == 'good' and list_of_commands[1] == 'bye':
                print('Good bye!')
                exit()
            elif list_of_commands[0] == 'show' and list_of_commands[1] == 'all':
                #print(f'!!!!!!!!, {self.dict}')
                for key, value in self.dict.items():
                    print(f'{key}: ')
                    for phone in value.phone_list:
                        print(f' {phone.value}')
            elif list_of_commands[0] == 'add':
                self.add_record(list_of_commands[1])
            elif list_of_commands[0] == 'find_name':
                self.find_by_name(list_of_commands[1])
            elif list_of_commands[0] == 'find_phone':
                self.find_by_phone(list_of_commands[1])
            elif list_of_commands[0] == 'phone':
                print(f"{list_of_commands[1]}: ")
                for phone in self.dict[list_of_commands[1]].phone_list:
                    print(f'\t {phone.value}')
            elif list_of_commands[0] == 'delete':
                self.dict[list_of_commands[1]].Delete()
                # print(contact_dict[list_of_commands[1]])
        elif len(list_of_commands) == 3:
            if list_of_commands[0] == 'add':
                self.add_record(list_of_commands[1], list_of_commands[2])
            elif list_of_commands[0] == 'change':
                self.dict[list_of_commands[1]].Edit(list_of_commands[2])
        else:
            print('I can\'t understand you')

    def input_error(self, user_input):
        #print('input error', user_input)
        try:
            if user_input[0] == '':
                raise Exception('string cannot be empty')
            elif user_input[0] == 'add':
                if len(user_input) < 3:
                    raise Exception('operator add error: name or phone number were missed')
                elif len(user_input) > 3:
                    raise Exception('operator add error: too much args')
            elif user_input[0] == 'hello' and len(user_input) > 1:
                raise Exception('operator hello error: hello must be a single operator')
            elif user_input[0] == 'change':
                if len(user_input) < 3:
                    raise Exception('operator change error: name or phone number were missed')
                elif len(user_input) > 3:
                    raise Exception('operator change error: too much args')
            elif user_input[0] == 'phone':
                if len(user_input) < 2:
                    raise Exception('operator phone error: name was missed')
                elif len(user_input) > 2:
                    raise Exception('operator phone error: too much args')
            elif user_input[0] == 'show' and user_input[1] == 'all':
                #print('input error, show all')
                if len(user_input) > 2:
                    raise Exception('operator show all error: show all must be a single operator')

            #print('input error, False')
            return False
        except Exception as e:
            print(e)
            return True
        except KeyError:
            return True
        except IndexError:
            return True

    def parcer(self):
        while True:
            user_input = input('>>> ').split(' ')
            #print('parcer', user_input)
            if self.input_error(user_input) == False:
                #print('parcer', user_input)
                return user_input
            else:
                pass
                #print('parcer pass')

def main():
    address_book = AddressBook()
    while True:
        address_book.process(address_book.parcer())

main()






