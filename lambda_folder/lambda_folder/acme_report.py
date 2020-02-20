from acme import product
import random

def generate_products(number_of_products=30):
    """
    generates number of given products in list
    """

    products = {} # empty list

    for i in range(number_of_products):
        # list of adjective and noun
        adj_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        noun_list = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
        adj = random.choice(adj_list)
        noun = random.choice(noun_list)

        # set defaults
        name = '{} {}'.format(adj, noun)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        products[i] = product(name,price,weight,flammability)
    return products

def inventory_report(products):
    """
    average of price, weight, flammability
    """
    # Empty list in order to append price, weight, flammability
    name_list = []
    price_list = []
    weight_list = []
    flammability_list = []

    # append and loop  
    for i in range(len(products)):
        name_list.append(products[i].name)
        price_list.append(products[i].price)
        weight_list.append(products[i].weight)
        flammability_list.append(products[i].flammability)

    unique_names = set(name_list)

    # function that calculates the average
    def average(y):
        return sum(y)/len(y)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ', len(unique_names))
    print('Average price: ', average(price_list))
    print('Average weight: ', average(weight_list))
    print('Average flammability: ', average(flammability_list))

if __name__ == '__main__':
    inventory_report(generate_products())
