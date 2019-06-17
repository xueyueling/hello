import pytest
import yaml


def analyze(file_name, key):
    with open(r"./data/" + file_name + ".yaml", "r") as f:
        data = yaml.load(f)
        data_list = list()
        data_list.extend(data[key].values())
        # for i in data[key].values():
        #     data_list.append(i)
        return data_list



        # {test_login: [{username:"zs", password: "zs"}, {username:"ls", password: "ls"}], test_login123: [[1, 2], [3, 4]}
        # {test_login:
        #       {test_login_001:
        #               {username: "zs", password: "zs123"}},
        #        test_login_002:
        #               {username: "ls", password: "ls123"}}}


        # [{username: "zs", password: "zs123"}, {username: "ls", password: "ls123"}]

class TestLogin:
    # @pytest.mark.parametrize(("name", "password"), analyze("test_login"))
    @pytest.mark.parametrize("args", analyze("login_data", "test_login"))
    def test_login(self, args):
        print(args)
        username = args["username"]
        password = args["password"]

        print(username)
        print(password)

    # @pytest.mark.parametrize(("age", "phone"), analyze("test_login123"))
    # def test_login123(self, age, phone):
    #     print(age)
    #     print(phone)
