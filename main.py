import time, random
customer_order = []
# Boba ordering chatbot, can take orders, give total, give suggestions, cater to allergies, give an estimated pickup time. 

class customerDrink():
  def __init__(self, drink_name, ice_level, sugar_level, price, topping):
    self.drink_name = drink_name
    self.ice_level = ice_level
    self.sugar_level = sugar_level
    self.price = price
    self.topping = topping
    
class Drink():
  def __init__(self, has_milk, has_caffeine, can_adjust_sugar, can_adjust_ice, price, can_serve_hot, ID):
    self.has_milk = has_milk
    self.has_caffeine = has_caffeine
    self.can_adjust_sugar = can_adjust_sugar
    self.can_adjust_ice = can_adjust_ice
    self.price = price
    self.can_serve_hot = can_serve_hot
    self.ID = ID
class MilkTea(Drink):
  def __init__(self, price, name, ID):
    self.name = name
    self.price = price
    self.ID = ID
    Drink.__init__(self, True, True, True, True, self.price, True, self.ID)

class FruitTea(Drink):
  def __init__(self, price, name, ID):
    self.name = name
    self.price = price
    self.ID = ID
    Drink.__init__(self, False, True, True, True, self.price, True, self.ID)

class IceBlended(Drink):
  def __init__(self, price, name, ID):
    self.name = name
    self.price = price
    self.ID = ID
    Drink.__init__(self, True, False, False, False, self.price, False, self.ID)

mangoGT = FruitTea('4.85', 'Mango Green Tea', 'A1')
passionGT = FruitTea('4.80', 'Passion Fruit Green Tea', 'A2')
strawberryGT = FruitTea('4.75', 'Strawberry Green Tea', 'A3')
grapefruitGT = FruitTea('4.65', 'Grapefruit Green Tea', 'A4')
peachGT = FruitTea('4.65', 'Peach Green Tea', 'A5')
fruit_teas = [mangoGT, passionGT, strawberryGT, grapefruitGT, peachGT]

oolongMT = MilkTea('4.50', 'Oolong Milk Tea', 'B1')
honeyMT = MilkTea('4.60', 'Honey Milk Tea', 'B2')
thaiMT = MilkTea('4.75', 'Thai Milk Tea', 'B3')
matchaMT = MilkTea('4.95', 'Matcha Milk Tea', 'B4')
brownMT = MilkTea('4.75', 'Brown Sugar Milk Tea', 'B5')
milk_teas = [oolongMT, honeyMT, thaiMT, matchaMT, brownMT]

oreoIB = IceBlended('5.75', 'Oreo Ice Blended', 'C1')
taroIB = IceBlended('5.50', 'Taro Ice Blended', 'C2')
coffeeIB = IceBlended('5.25', 'Coffee Ice Blended', 'C3')
coconutIB = IceBlended('5.25', 'Coconut Ice Blended', 'C4')
pineappleIB = IceBlended('5.45', 'Pineapple Ice Blended', 'C5')
ice_blendeds = [oreoIB, taroIB, coffeeIB, coconutIB, pineappleIB]

full_menu = []
[full_menu.extend(i) for i in (milk_teas, fruit_teas, ice_blendeds)]

toppings = {'Boba': '0.50', 'Pudding': '0.50', 'Lychee Jelly': '0.50', 'Mango Popping Boba': '0.50', 'Cheese Foam': '0.50'}

def print_sep():
  print('---------------=+=---------------')
def print_menu():
  print()
  print('-' * 15 + 'MENU' + '-' * 15)
  print('-FRUIT TEA-')
  for i in fruit_teas:
    print(i.ID + '  ' + i.name + (' ' * (30 - 5 - len(i.name))) + '$' + i.price)
  print()
  print('-MILK TEA-')
  for i in milk_teas:
    print(i.ID + '  ' + i.name + (' ' * (30 - 5 - len(i.name))) + '$' + i.price)
  print()
  print('-ICE BLENDED-')
  for i in ice_blendeds:
    print(i.ID + '  ' + i.name + (' ' * (30 - 5 - len(i.name))) + '$' + i.price)
  print()
  print('-TOPPINGS-')
  for top, price in toppings.items():
    print(top + (' ' * (34 - 5 - len(top))) + '$' + price)
  print()
def greet():
  print('Hello! Welcome to Kate\'s Boba Shop. We have many delicous drinks! Here is our menu.')
  time.sleep(2)
  print_menu()
  time.sleep(5)
  choice = input('Would you like to (o)rder now or would you like some (s)uggestions? ').lower()
  if choice == 'o':
    take_order()
  else:
    provide_suggestion()
  
def goodbye(name):
  print(f'Order for {name} ready at the counter!')
  order = []
  time.sleep(1)
  another = input('Would you like to place another order today?')
  if another == 'yes':
    print()
    order()
  else:
    print('Thank you so much for visiting Kate\'s Boba Shop! We hope you visit again')
  
def take_order():
  global order
  take_order = True
  while take_order:
    drinkID = input('What would you like to order? Please indicate using the drink IDs on our menu. ').upper()
    for i in full_menu:
      if i.ID == drinkID:
        drink_name = i.name
        price = float(i.price) + 0.5
        break
    print('Yum! The ' + drink_name + ' is one of my favorites!\n')  
    time.sleep(0.5)
    ice_level = input('What ice level would you like for your ' + drink_name + '? Low, Regular, or Extra? ').lower()
    sweet_level = input('What sugar level would you like for your ' + drink_name + '? Low, Regular, or Extra? ').lower()
    toppings = input('What topping would you like in your ' + drink_name + '? ')
    drink = customerDrink(drink_name, ice_level, sweet_level, price, toppings)
    confirm = input(f'Ok so that\'s a {drink_name}, {ice_level} ice, {sweet_level} sweet, with {toppings}. Is your order correct? ').lower()
    if confirm == 'yes':
      customer_order.append(drink)
      again = input('Would you like to order another drink?').lower()
      if again == 'yes':
        take_order = True
      else:
        take_order = False
    else:
      print('Oh... I\'m so sorry about that, let me get your order again')
      take_order = True
  print('Ok! We will proceed to checkout.\n')
  give_total()
def give_total():
  total = 0
  print('You ordered...\n')
  for i in customer_order:
    total += float(i.price)
    print(f'{i.drink_name}, {i.ice_level} ice, {i.sugar_level} sweet, with {i.topping}')
  print('\nThat comes out to', total)
  name = input('\nCan I get a name for your order?')
  print('Thank you! Your order will be out shortly')
  for i in range(3):
    time.sleep(1.5)
    print('...')
  goodbye(name)

  
def provide_suggestion():
  suggest = []
  int1 = random.randint(1,3)
  if int1 == 1:
    wantMilk = input('Do you like drinks with milk in them? ').lower()
    
    if wantMilk == 'yes':
      for i in full_menu:
        if i.has_milk == True:
          suggest.append(i.name)
    else: 
      for i in full_menu:
        if i.has_milk == False:
          suggest.append(i.name)  
          
  elif int1 == 2:
    want_caffeine = input('Do you want a drink that has caffeine in it? ').lower()
  
    if want_caffeine == 'yes':
      for i in full_menu:
        if i.has_caffeine == True:
          suggest.append(str(i.name))
    else: 
      for i in full_menu:
        if i.has_caffeine == False:
          suggest.append(str(i.name)) 
  else:
    wantHot = input('Would you like a drink to warm you up? ').lower()
    
    if wantHot == 'yes':
      for i in full_menu:
        if i.can_serve_hot == True:
          suggest.append(i.name + ' warmed')
    else: 
      for i in full_menu:
        if i.can_serve_hot == False:
          suggest.append(i.name)
      
  print('\nHmm.... Let me think...')
  time.sleep(1.5)
  print('I suggest you order the ~' + suggest.pop(random.randint(0,len(suggest) - 1)) + '~')
  orderOrNew = input('Would you like (a)nother suggestion or are you (r)eady to order?').lower()
  print()
  while orderOrNew == 'a':
    if len(suggest) == 0:
      print('Sorry, I am out of suggestions. Let me take your order now. \n')
      break
    print('I suggest you order the... ~' + suggest.pop(random.randint(0,len(suggest) - 1)) + '~')
    orderOrNew = input('Would you like (a)nother suggestion or are you (r)eady to order? ').lower()
    print()
  take_order()

def order():
  greet()

#interaction
order()

