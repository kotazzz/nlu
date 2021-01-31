import random
import uuid

from NewLifeUtils.UtilsModule import safe_format
from NewLifeUtils.StringUtilModule import parse_args
from NewLifeUtils.LoggerModule import *
from NewLifeUtils.TableBuildModule import *


def create_value(vartype, *params):
    print()
    if vartype == "int":
        if len(params) == 2:
            return random.randint(list(params)[0], list(params)[1])
        else:
            return random.randint(1, 1000)

    elif vartype == "bool":
        return random.choice([True, False])

    elif vartype == "uid":
        return (uuid.UUID(bytes=random.randbytes(16)))

    elif vartype == "name":
        return random.choice(["Abraham", "Adam", "Adrian", "Albert", "Alexander", "Alfred",
                              "Anderson", "Andrew", "Anthony", "Arnold", "Arthur", "Ashley", "Austen",
                              "Benjamin", "Bernard", "Brian", "Caleb", "Calvin", "Carl", "Chad",
                              "Charles", "Christian", "Christopher", "Clayton", "Clifford", "Clinton",
                              "Corey", "Cory", "Daniel", "Darren", "David", "Derek", "Dirk", "Donald",
                              "Douglas", "Dwight", "Earl", "Edgar", "Edmund", "Edward", "Edwin", "Elliot",
                              "Eric", "Ernest", "Ethan", "Ezekiel", "Felix", "Franklin", "Frederick",
                              "Gabriel", "Gareth", "Geoffrey", "Gerald", "Graham", "Grant", "Gregory",
                              "Harold", "Harry", "Henry", "Herbert", "Horace", "Hubert", "Hugh", "Ian",
                              "Jack", "Jacob", "James", "Jason", "Jasper", "Jerome", "Jesse", "John",
                              "Jonathan", "Joseph", "Joshua", "Julian", "Keith", "Kenneth", "Kevin",
                              "Kurt", "Kyle", "Lawrence", "Leonard", "Lester", "Louis", "Lucas",
                              "Malcolm", "Marcus", "Marshall", "Martin", "Matthew", "Maximilian",
                              "Michael", "Miles", "Nathan", "Neil", "Nicholas", "Norman", "Oliver",
                              "Oscar", "Oswald", "Otto", "Owen", "Patrick", "Paul", "Peter", "Philip",
                              "Quentin", "Randall", "Raphael", "Raymond", "Richard", "Robert",
                              "Roderick", "Rodger", "Rodney", "Ronald", "Rory", "Rufus", "Rupert",
                              "Russell", "Samuel", "Scott", "Sebastian", "Shayne", "Sigmund", "Simon",
                              "Stephen", "Steven", "Sylvester", "Terence", "Thomas", "Timothy", "Tobias",
                              "Travis", "Tristan", "Tyler", "Valentine", "Victor", "Vincent", "Walter",
                              "Wayne", "Wilfred", "William", "Winston", "Zachary"])
    else:
        return '{' + str(vartype) + '}'


ex = {
    "id": "{uid}",
    "id2": "{uid}",
    "name": "{name}",
    "int": "{int}",
    "int2": "{int2}",
}


def obj_from_template(rawobj):
    names = {
        "int": create_value("int"),
        "bool": create_value("bool"),
        "uid": create_value("uid"),
        "name": create_value("name"),
    }
    for key in rawobj:
        rawobj[key] = safe_format(rawobj[key], func=create_value)
    return rawobj


from pprint import pprint
err('hi')

# pprint(obj_from_template(ex))
def sumfunc(a, b):
    return int(a) + int(b)

print(safe_format('{sum 1 2} - {sum 1 2}', smart={"sum": sumfunc}))
log("Что то случилось")
wrn("Что то случилось")
err("Что то случилось")
tip("Что то случилось")
rea("Это я уже ввел - ")
log(create_table(2,[],["1","2222222","text","text","text","text","text","text"]))
rea("Это я сейчас пишу")