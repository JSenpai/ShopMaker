#Importing tis a bitch

from tkinter import *
import random
from random import choice
import tkinter.messagebox
from tkinter import Frame


class Main:

    def __init__(self, master):
        frame_main = Frame(master)
        frame_bottom = Frame(master)
        frame_main.pack(side=TOP)
        frame_bottom.pack()


        #Main Frame
        self.titleLabel = Label(frame_main, text="Welcome to the Shop Generator/Populator.\n"
                                                 "please Use the selectons below to Make your shop/stall."
                                                 "\n")
        self.titleLabel.grid(columnspan=10)

        #Establishments
        self.estabLabel = Label(frame_main, text='Establishment Type:')
        self.estabLabel.grid(row=1)

        establishments = ('Shop', 'Stall', 'Traveling Merchant')
        self.varEstab = StringVar()
        self.varEstab.set('Shop')
        self.establishment = OptionMenu(frame_main, self.varEstab, *establishments)
        self.establishment.configure(font='Arial' '12')
        self.establishment.grid(row=2)

        #Shop Type
        self.shopTypeLabel = Label(frame_main, text='Shop Type:')
        self.shopTypeLabel.grid(row=1, column=3)

        shopTypes = ('Water-side Dealer', 'Tailor', 'Stonecutter', 'Shady Dealer', 'Potion Shop', 'Magical Dealer',
                     'Leather Worker', 'General Store', 'Faith Supplies', 'Bowyer', 'Art & Games', 'Blacksmith',
                     'Arcane Shop', 'Adventuring Supplies')
        self.varShopType = StringVar()
        self.varShopType.set('Water-side Dealer')
        self.shopType = OptionMenu(frame_main, self.varShopType, *shopTypes)
        self.shopType.configure(font='Arial' '12')
        self.shopType.grid(row=2, column=3)

        #Shop Size
        self.shopSizeLabel = Label(frame_main, text='Shop Size:')
        self.shopSizeLabel.grid(row=1, column=5)

        shopSizes = ('Small', 'Medium', 'Large', 'Custom')
        self.varShopSize = StringVar()
        self.varShopSize.set('Small')
        self.shopSize = OptionMenu(frame_main, self.varShopSize, *shopSizes)
        self.shopSize.configure(font='Arial' '12')
        self.shopSize.grid(row=2, column=5)

        #Generator Button
        self.genButton = Button(frame_main, text='Generate', font='Arial' '12', command=self.Generate)
        self.genButton.grid(row=4, column=3)


        #Bottom Frame
        self.quitButton = Button(frame_bottom, text='Quit', bg='black', fg='white',width=10, command=quit)
        self.quitButton.pack(side=BOTTOM)


        #Status Bar
        statusbar = Label(master, text='Main Window', bd=1, relief=SUNKEN, anchor=W)
        statusbar.pack(side=BOTTOM, fill=X)


        #Generator

    def Generate(self):
        window = Toplevel()
        window.title('Generated Shop')

        self.estab = self.varEstab.get()
        self.shop = self.varShopType.get()
        self.size = self.varShopSize.get()

        #Frames

        mainFrame = Frame(window)
        midFrame = Frame(window)
        botFrame = Frame(window)

        mainFrame.pack(side=TOP)
        midFrame.pack()
        botFrame.pack(side=BOTTOM)

        #Main frame Establishment type and shop type

        shopTitle = Label(mainFrame, text=self.estab+' '+self.shop)
        shopTitle.configure(font='Arial' '18')
        shopTitle.pack()

        #Middle Frame Handles shop inventory

        #Lists for each shop

        watersidedealer_inv = ['Spear - 1 gp', 'Net - 1 gp', 'Fishing Tackle - 1 gp', 'Rowboat - 50 gp',
                               '1 lb. of Fishing Bait - 5 cp']
        tailor_inv = ['Backpack - 2 gp', 'Basket - 4 sp', 'Bedroll - 1 gp', 'Blanket - 5 sp',
                      'Clothes, Common - 5 sp', 'Clothes, Costume - 5 gp', 'Clothes, Fine - 15 gp',
                      'Clothes, Traveler - 2 gp', 'Component Pouch - 25 gp', 'Pouch - 5 sp', 'Robes - 1 gp',
                      'Sack - 1 cp', 'Tent, 2-Person - 2 gp', "Weaver's Tools - 1 gp"]
        stonecutter_inv = ['Amulet/Necklace, Exquisite - 5 gp', 'Amulet/Necklace, Mundane - 5 sp',
                           'Arcane Focus, Crystal - 10 gp', 'Arcane Focus, Orb - 20 gp', 'Earrings, Exquisite - 4 gp',
                           'Earrings, Mundane - 4 sp', 'Jewelry - 50 gp + Gem Value', 'Ring, Exquisite - 3 gp',
                           'Ring, Mundane - 3 sp', 'Signet Ring - 5 gp', "Jeweler's Tools - 25 gp"]
        shadydealer_inv = ['Acid (Vial) - 25 gp', 'Antitoxin (Vial) - 50 gp', 'Caltrops (20) - 1 gp',
                           'Clothes, Costume - 5 gp', 'Manacles - 1 gp', 'Oil (Flask) - 1 sp',
                           'Poison, Basic (Vial) - 100 gp', 'Ram, Portable - 4 gp', 'Spikes, Iron (10) - 1 gp',
                           'Disguise Kit - 25 gp', 'Forgery Kit - 15 gp', 'Dice set - 1 sp', 'Playing Card set - 5 sp',
                           "Poisoner's Kit - 50 gp", "Thieve's Tools - 25 gp"]
        potionshop_inv = ['Acid (Vial) - 25 gp', "Alchemist's Fire (Flask) - 50 gp", 'Antitoxin (Vial) - 50 gp',
                          'Bottle, Glass - 2 gp', 'Component Pouch - 25 gp', 'Flask - 2 cp', "Healer's Kit - 5 gp",
                          'Ink (1 oz. Bottle) - 10 gp', 'Jug - 2 cp', 'Oil (Flask) - 1 sp', 'Perfume (Vial) - 5 gp',
                          'Poison, Basic (Vial) - 100 gp', 'Potion of Healing - 50 gp', 'Vial - 1 gp',
                          "Alchemist's Supplies - 50 gp", "Brewer's Supplies - 20 gp", "Cook's Supplies - 1 gp",
                          'Herbalism Kit - 5 gp', "Poisoner's Kit - 50 gp", 'Potion, Common - 50 gp',
                          'Potion, Uncommon - 250 gp', 'Potion, Rare - 2500 gp']
        magicaldealer_inv = ['Arcane Focus, Crystal - 10 gp', 'Arcane Focus, Orb - 20 gp', 'Arcane Focus, Rod - 10 gp',
                             'Arcane Focus, Staff - 10 gp', 'Arcane Focus, Wand - 10 gp', 'Component Pouch - 25 gp',
                             'Potion of Healing - 50 gp', 'Spellbook - 50 gp']
        leatherworker_inv = ['Light Armor, Leather - 10 gp', 'Light Armor, Studded - 45 gp',
                             'Medium Armor, Hide - 10 gp', 'Shield - 10 gp', 'Sling - 1sp', 'Water-skin - 2 sp',
                             "Cobbler's Tools - 5 gp", "Leatherworker's Tools - 5 gp", 'Bagpipes - 30 gp',
                             'Drum - 6gp']
        generalstore_inv = ['Abacus - 2 gp', 'Barrel - 2 gp', 'Blanket - 5 sp', 'Bottle, Glass - 2 gp', 'Bucket - 5 cp',
                            'Candle - 1 cp', 'Chest - 5 gp', 'Clothes, Common - 5  sp', 'Clothes, Fine - 15 gp',
                            'Flask/Tankard - 2 cp', 'Hammer - 1 gp', 'Ink (1 oz. Bottle) - 10 gp', 'Ink Pen - 2 cp',
                            'Jug/Pitcher - 2 cp', 'Ladder (10ft.) - 1 sp', 'Lantern, Hooded - 5 gp', 'Lock - 10 gp',
                            'Mess Kit - 2 sp', 'Mirror, Steel - 5 gp', 'Paper (1 Sheet), 1 sp', 'Pick, Miner - 2 gp',
                            'Pot, Iron - 2 gp', 'Pouch - 5 sp', 'Rope, Hemp (50ft.) - 1 gp',
                            'Rope, Silk (50ft.) - 10 gp', 'Sack - 1 cp', 'Scale, Merchant - 5 gp', 'Shovel - 2 gp',
                            'Signent Ring - 5 gp', 'Soup - 2 cp', 'Vial - 1 gp', "Carpenter's Tools - 15 gp",
                            "Cobbler's Tools - 25 gp", "Cook's Utensils - 50 gp", "GlassBlower's Tools - 30 gp",
                            "Leatherworker's'Tools - 5 gp", "Mason's Tools - 10 gp", "Potter's Tools - 10 gp",
                            "Smith's Tools - 20 gp", "Weaver's Tools - 1 gp", "Woodcarver's Tools - 1 gp"]
        faithsupplies_inv = ['Aims Box - 5 gp', 'Bell - 1 gp', 'Blanket - 5 sp', 'Book, Scripture - 25 gp',
                             'Candle - 1 cp', 'Case, Map/Scroll - 1 gp', 'Censer - 5 gp', 'Chalk (1 Piece) - 1cp',
                             'Flask - 2cp', "Healer's Kit - 5 gp", 'Holy Symbol, Amulet - 5 gp',
                             'Holy Symbol, Emblem - 5 gp', 'Holy Symbol, Reliquary - 5 gp',
                             'Holy Water ( Flask) - 25 gp', 'Incense (1 oz. Block) - 1 cp', 'Ink (1 oz. Bottle) - 10 gp',
                             'Ink Pen - 2 cp', 'Lamp - 5 sp', 'Lantern, Hooded - 5 gp', 'Oil (Flask) - 1  sp',
                             'Paper (1 Sheet) - 2 sp', 'Parchment (1 Sheet) - 1 sp', 'Perfume (Vial) - 5 gp',
                             'Potion of Healing - 50 gp', 'Rations (1 Day) - 5 sp', 'Torch - 1 cp', 'Vial - 1 gp',
                             'Water-skin - 2 sp', "Calligrapher's Supplies - 1- gp", 'Herbalism Kit - 5 gp',
                             'Flute - 2 gp', 'Lyre - 30 gp', 'Horn - 3 gp',
                             'Spell Service, Cure Wounds (1st Lvl) - 10 gp',
                             'Spell Service, Gentle Repose (1st Lvl) - 50gp',
                             'Spell Service, Lesser Restoration (2nd Lvl) - 50 gp',
                             'Spell Service, Remove Curse (3rd Lvl) - 100 gp',
                             'Spell Service, Revivify (3rd Lvl) - 400 gp',
                             'Spell Service, Raise Dead (5th Lvl) - 1,000 gp']
        bowyer_inv = ['Crossbow, Light - 25 gp', 'Shortbow - 25gp', 'Crossbow, Hand - 75 gp',
                      'Crossbow, Heavy - 50 gp', 'Longbow - 50 gp', 'Arrows (20) - 1 gp',
                      'Crossbow Bolts (20) - 1 gp', 'Case, Crossbow Bolt - 1 gp', 'Quiver - 1gp']
        artgames_inv = ["Calligrapher's Supplies - 10 gp", "GlassBlower's Tools - 30 gp", "Painter's Supplies - 10 gp",
                        "Potter's Tools - 10 gp", "Weaver's Tools - 1 gp", "Woodcarver's Tools - 1 gp",
                        'Disguise Kit - 25 gp', 'Dice Set - 1 sp', 'DragonChess Set- 1 gp', 'Playing Card Set - 5 sp',
                        '3-Dragon Ante Set - 1 gp', 'Bagpipes - 30 gp', 'Drum - 6 gp', 'Dulcimer - 25 gp',
                        'Flute - 2 gp', 'Lute - 35 gp', 'Horn - 3 gp', 'Pan-Flute - 12 gp',
                        'Shawm - 2 gp', 'Viol - 30 gp']
        blacksmith_inv = ['Light Armor, Studded - 45gp', 'Medium Armor, Chain-Shirt - 50 gp',
                          'Medium Armor, Scalmail - 50 gp', 'Medium Armor, Breastplate - 400 gp',
                          'Medium Armor, Half-Plate - 750 gp', 'Heavy Armor, Ring Mail - 30 gp',
                          'Heavy Armor, Chain Mail - 75 gp', 'Heavy Armor, Splint - 200 gp',
                          'Heavy Armor, Plate - 1,500 gp', 'Shield - 10 gp', 'Dagger - 2 gp',
                          'Handaxe - 5 gp', 'Javelin - 5 gp', 'Light Hammer - 2 gp', 'Mace - 5 gp',
                          'Sickle - 1 gp', 'Spear - 1 gp ', 'Battleaxe - 10 gp', 'Flail - 10 gp', 'Glaive - 20 gp',
                          'Greataxe - 30 gp', 'Greatsword - 50 gp', 'Halberd - 20 gp', 'Lance - 20 gp',
                          'LongSword - 15 gp', 'Maul - 15 gp', 'Morningstar - 15 gp', 'Pike - 5 gp',
                          'Rapier - 25  gp', 'scimitar - 25 gp', 'ShortSword - 10 gp', 'Trident - 5 gp',
                          'Warpick - 5 gp', 'Ball Bearings (1,000) - 1 gp', 'Bell - 1 gp',
                          'Block and Tackle - 1 gp', 'Chain (10ft.) - 5 gp', 'Crowbar - 2 gp',
                          'Grappling Hook - 2 gp', 'Hammer - 1 gp', 'Hammer, Sledge - 2 gp',
                          'Hunting Trap - 5 gp', 'Lamp - 5 sp', 'Lantern, Bullseye - 10 gp', 'Lantern, Hooded - 5 gp',
                          'Lock - 10 gp', 'Manacles - 2 gp', 'Mirror, Steel - 5 gp', 'Pick, Miner - 2 gp',
                          'Piton - 5 cp', 'Pot, Iron - 2 gp', 'Spikes, Iron 1 gp', 'Whetstone - 1cp',
                          "Carpenter's Tools - 8 gp", "Mason's Tools - 10gp", "Smith's Tools - 20 gp",
                          "Tinker's Tools - 50 gp", 'Horn - 3 gp']
        arcaneshop_inv = ['Quarterstaff - 2 sp', 'Abacus - 2 gp', 'Arcane Focus, Crystal - 10 gp',
                          'Arcane Focus, Orb - 20 gp', 'Arcane Focus, Rod - 10 gp', 'Arcane Focus, Staff - 5 gp',
                          'Arcane Focus, Wand - 10 gp', 'Bottle, glass - 2 gp', 'Candle - 1 cp',
                          'Case, Map or Scroll - 1 gp', 'Component Pouch - 25 gp',
                          'Druidic Focus, Sprig of Mistletoe - 1 gp', 'Druidic Focus, Totem - 1 gp',
                          'Druidic Focus, Wooden Staff - 5 gp', 'Druidic Focus, Yew Wand - 10 gp', 'Hourglass - 25 gp',
                          'Ink (1 ounce bottle) - 10 gp', 'Ink Pen - 2 cp', 'Paper (one sheet) - 2 sp',
                          'Parchment (one sheet) - 1 sp', 'Pouch - 5 sp', 'Robes - 1 gp', 'Spellbook - 50 gp',
                          'Vial - 1 gp', "Alchemist's Supplies - 50 gp", "Calligrapher's Suplies - 10 gp",
                          'Lute - 35 gp', 'Lyre - 30 gp', 'Spell Scroll, Common (Cantrip) - 50 gp',
                          'Spell Scroll, Common (Level 1) - 100 gp', 'Spell Scroll, Uncommon (Level 2) - 250 gp',
                          'Spell Scroll, Uncommon (Level 3) - 500 gp', 'Spell Scroll, Rare (Level 4) - 2500 gp',
                          'Spell Scroll, Rare (Level 5) - 5000 gp', 'Service, Magic Appraisal (Identify) - 100 gp']
        adventsupplies_inv = ['Light Armor, Padded - 5 gp', 'Light Armor, Leather - 10 gp',
                              'Light Armor, Studded Leather - 45 gp', 'Medium Armor, Hide - 10 gp', 'Club - 1 sp',
                              'Dagger - 2 gp', 'Greatclub - 2 sp', 'Handaxe - 5 gp', 'Light Hammer - 2 gp',
                              'Quarterstaff - 2 sp', 'Crossbow, Light - 25 gp', 'Dart - 5 cp', 'Shortbow - 25 gp',
                              'Sling - 1 sp', 'Whip - 2 gp', 'Blowgun - 10 gp', 'Crossbow, Hand - 75 gp',
                              'Crossbow, Heavy - 50 gp', 'Longbow - 50 gp', 'Arrows (20) - 1gp',
                              'Blowgun Needles (50) - 1 gp', 'Crossbow Bolts (20) - 1 gp', 'Sling Bullets (20) - 4 cp',
                              'Backpack - 2 gp', 'Bedroll - 1 gp', 'Blanket - 5 sp', 'Block and Tackle - 1 gp',
                              'Bottle, Glass - 2 gp', 'Candle - 1 cp', 'Case, Crossbow Bold - 1 gp',
                              'Case, Map or Scroll - 1 gp', 'Chain (10 feet) - 5 gp', 'Chest - 5 gp',
                              "Climber's Kit - 25 gp", "Clothes, Traveler's - 2 gp", 'Crowbar - 2 gp',
                              'Flask or Tankard - 2cp', 'Grappling Hook - 2 gp', 'Hammer - 1 gp', "Healer's Kit - 5 gp",
                              'Hourglass - 25 gp', 'Hunting Trap - 5 gp', 'Ink (1 ounce bottle) 10 gp', 'Ink Pen - 2 cp',
                              'Jug or Pitcher - 2 cp', 'Ladder (10-foot) - 1 sp', 'Lantern, Bullseye - 10 gp',
                              'Lantern, Hooded - 5 gp', 'Lock - 10 gp', 'Mess Kit - 2 sp', 'Mirror, Steel - 5gp',
                              'Paper (one sheet) - 2 sp', 'Parchment (one sheet) - 1 sp', "Pick, Miner's - 2 gp",
                              'Piton - 5 gp', 'Pole (10-foot) - 5 cp', 'Pot, Iron - 2 gp', 'Pouch - 5 sp',
                              'Quiver - 1 gp', 'Rations (1 day) - 5 sp', 'Rope, Hempen (50 feet) - 1 gp',
                              'Rope, Silk (50 feet) - 10 gp', 'Sack - 1 cp', 'Shovel - 2 gp', 'Signal Whistle - 5 cp',
                              'Signet Ring - 5 gp', 'Spyglass - 1000 gp', 'Tent, Two-person - 2 gp', 'Tinderbox - 5 sp',
                              'Torch - 1 cp', 'Vial - 1 gp', 'Waterskin - 2 sp', "Cartographer's Tools - 15 gp",
                              "Jeweler's Tools - 25 gp", "Tinker's Tools - 50 gp", "Herbalism Kit - 5 gp",
                              "Navigator's Tools - 25 gp"]

        #Function for generating the inventory

        if self.shop == 'Adventuring Supplies':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(adventsupplies_inv)+'\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(adventsupplies_inv)+'\n'
                self.shopOutputLabel = Label(midFrame, text= ''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(adventsupplies_inv)+'\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            else:
                self.customEntry = Entry(midFrame)
                self.customEntry.pack()
                shopOutput = ['0']*self.customEntry
                for x in range(0, self.customEntry):
                    shopOutput[x] = random.choice(adventsupplies_inv)+'\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == "Arcane Shop":
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(arcaneshop_inv)+'\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(arcaneshop_inv)+'\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(arcaneshop_inv)+'\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'Blacksmith':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(blacksmith_inv)+'\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(blacksmith_inv)+'\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(blacksmith_inv)+'\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'Art & Games':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(artgames_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(artgames_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(artgames_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == "Bowyer":
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(bowyer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(bowyer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(bowyer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'Faith Supplies':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(faithsupplies_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(faithsupplies_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(faithsupplies_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'General Store':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(generalstore_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(generalstore_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(generalstore_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'Leather Worker':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(leatherworker_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(leatherworker_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(leatherworker_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'Magical Dealer':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(magicaldealer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(magicaldealer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(magicaldealer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'Potion Shop':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(potionshop_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(potionshop_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(potionshop_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'Shady Dealer':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(shadydealer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(shadydealer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(shadydealer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'Stonecutter':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(stonecutter_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(stonecutter_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(stonecutter_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'Tailor':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(tailor_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(tailor_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(tailor_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
        elif self.shop == 'Water-side Dealer':
            if self.size == 'Small':
                shopOutput = ['0']*10
                for x in range(0, 10):
                    shopOutput[x] = random.choice(watersidedealer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Medium':
                shopOutput = ['0']*15
                for x in range(0, 15):
                    shopOutput[x] = random.choice(watersidedealer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()
            elif self.size == 'Large':
                shopOutput = ['0']*20
                for x in range(0, 20):
                    shopOutput[x] = random.choice(watersidedealer_inv) + '\n'
                self.shopOutputLabel = Label(midFrame, text=''.join(shopOutput))
                self.shopOutputLabel.configure(font='Arial' '12' 'bold')
                self.shopOutputLabel.pack()

        #Bottom Frame

        #Bottom Frame
        self.quitButton = Button(botFrame, text='Quit', bg='black', fg='white',width=10, command=quit)
        self.quitButton.pack(side=BOTTOM)




root = Tk()
a = Main(root)
root.title('Shop Directory')
root.mainloop()


