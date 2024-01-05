class Persons:
    names = []

    def set_name(self, user_name):
        self.names.append(user_name)
        return len(self.names) - 1

    def get_name(self, user_id):
        if user_id >= len(self.names):
            return 'There is no such user'
        else:
            return self.names[user_id]

    def del_name(self, user_name):
        for i in range(len(self.names)):
            if user_name == self.names[i]:
                self.names.remove(user_name)
                return True
        return False


if __name__ == '__main__':
    person = Persons()
