#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:25:26 2022

@author: nasimnassar
"""

from tkinter import *
import tkinter as tk


class OccupyEvolutionApp:

    def __init__(self, root):

        root.title("OccupyEvolution")

        frame = Frame(root, borderwidth=2, relief="sunken")
        frame.grid(column=1, row=1, sticky=(N, E, S, W))
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)
        
        ### Column 1: Functions ###
        
        # Import Libraries
        libraries_label = Label(frame, text="Libraries")
        libraries_label.grid(column=1, row=1, sticky=(W))
        libraries_button = Button(frame, text="Import", command=self.import_libraries)
        libraries_button.grid(column=1, row=2, sticky=(W))
        
        # Load Database
        database_label = Label(frame, text="Database")
        database_label.grid(column=1, row=3, sticky=(W))
        database_button = Button(frame, text="Load Database", command=self.load_database)
        database_button.grid(column=1, row=4, sticky=(W))
        
        # Create Starting Population
        create_starting_population_label = Label(frame, text="Starting Population")
        create_starting_population_label.grid(column=1, row=5, sticky=(W))
        create_starting_population_button = Button(frame, text="Create", command=self.create_starting_population)
        create_starting_population_button.grid(column=1, row=6, sticky=(W))
        
        #Create First Generation from generation zero
        create_first_generation_label = Label(frame, text="First Generation")
        create_first_generation_label.grid(column=1, row=7, sticky=(W))
        create_first_generation_button = Button(frame, text="Create", command=self.create_first_generation)
        create_first_generation_button.grid(column=1, row=8, sticky=(W))
        
        # Create Next Generation
        create_next_generation_label = Label(frame, text="Next Generation")
        create_next_generation_label.grid(column=1, row=9, sticky=(W))
        create_next_generation_button = Button(frame, text="Create", command=self.create_next_generation)
        create_next_generation_button.grid(column=1, row=10, sticky=(W))
        
        ### Column 2: Radio Buttons ###
        
        ## Operating System OS
        OS_label = Label(frame, text="Win or Mac")
        OS_label.grid(column=2, row=1, sticky=(W, E))
        self.OS_selected_value = tk.IntVar()
        OS_radiobutton1 = Radiobutton(frame, text="Windows", padx=5, pady=5, variable=self.OS_selected_value, value=1)
        OS_radiobutton1.grid(column=2, row=2, sticky=(W))
        OS_radiobutton2 = Radiobutton(frame, text="Mac", padx=5, pady=5, variable=self.OS_selected_value, value=0)
        OS_radiobutton2.grid(column=2, row=2, sticky=(E))
        #OS_selected_value = OS_radiobutton2.insert(0, 2.0)
        self.OS_selected_value.set("0")
        
        ## Display demographic figures DDF
        display_demographic_figures_label = Label(frame, text="Display Demographic Figures")
        display_demographic_figures_label.grid(column=2, row=3, sticky=(W, E))
        self.DDF_selected_value = tk.IntVar()
        DDF_radiobutton1 = Radiobutton(frame, text="On", padx=5, pady=5, variable=self.DDF_selected_value, value=1)
        DDF_radiobutton1.grid(column=2, row=4, sticky=(W))
        DDF_radiobutton2 = Radiobutton(frame, text="Off", padx=5, pady=5, variable=self.DDF_selected_value, value=0)
        DDF_radiobutton2.grid(column=2, row=4, sticky=(E))
        self.DDF_selected_value.set("0")
        
        ## Manual or Automatic AG #many generations in 1 click or 1by1
        automatic_generations_label = Label(frame, text="Automatic Generations")
        automatic_generations_label.grid(column=2, row=5, sticky=(W, E))
        self.AG_selected_value = tk.IntVar()
        AG_radiobutton1 = Radiobutton(frame, text="On", padx=5, pady=5, variable=self.AG_selected_value, value=1)
        AG_radiobutton1.grid(column=2, row=6, sticky=(W))
        AG_radiobutton2 = Radiobutton(frame, text="Off", padx=5, pady=5, variable=self.AG_selected_value, value=0)
        AG_radiobutton2.grid(column=2, row=6, sticky=(E))
        self.AG_selected_value.set("0")
        
        ## Occupation Inheritance OI
        occupation_inheritance_label = Label(frame, text="Occupation Inheritance")
        occupation_inheritance_label.grid(column=2, row=7, sticky=(W, E))
        self.OI_selected_value = tk.IntVar()
        OI_radiobutton1 = Radiobutton(frame, text="On", padx=5, pady=5, variable=self.OI_selected_value, value=1)
        OI_radiobutton1.grid(column=2, row=8, sticky=(W))
        OI_radiobutton2 = Radiobutton(frame, text="Off", padx=5, pady=5, variable=self.OI_selected_value, value=0)
        OI_radiobutton2.grid(column=2, row=8, sticky=(E))
        self.OI_selected_value.set("1")
        
        ## Display real data percentages DRDP
        display_real_data_percentages_label = Label(frame, text="Display Real Data Percentages")
        display_real_data_percentages_label.grid(column=2, row=9, sticky=(W, E))
        self.DRDP_selected_value = tk.IntVar()
        DRDP_radiobutton1 = Radiobutton(frame, text="On", padx=5, pady=5, variable=self.DRDP_selected_value, value=1)
        DRDP_radiobutton1.grid(column=2, row=10, sticky=(W))
        DRDP_radiobutton2 = Radiobutton(frame, text="Off", padx=5, pady=5, variable=self.DRDP_selected_value, value=0)
        DRDP_radiobutton2.grid(column=2, row=10, sticky=(E)) # Error in bar plot!
        self.DRDP_selected_value.set("0")
        
        ## Display population data DPD
        display_population_data_label = Label(frame, text="Display Population Data")
        display_population_data_label.grid(column=2, row=11, sticky=(W, E))
        self.DPD_selected_value = tk.IntVar()
        DPD_radiobutton1 = Radiobutton(frame, text="On", padx=5, pady=5, variable=self.DPD_selected_value, value=1)
        DPD_radiobutton1.grid(column=2, row=12, sticky=(W))
        DPD_radiobutton2 = Radiobutton(frame, text="Off", padx=5, pady=5, variable=self.DPD_selected_value, value=0)
        DPD_radiobutton2.grid(column=2, row=12, sticky=(E))
        self.DPD_selected_value.set("0")
        
        ### Column 3: Parameters ###
        
        ## Parameters Label
        parameters_label = Label(frame, text="Parameters")
        parameters_label.grid(column=3, row=1, sticky=(W, E))
        
        ## Starting Population SP
        starting_population_label = Label(frame, text="Starting Population Size")
        starting_population_label.grid(column=3, row=2, sticky=(W))
        self.SP_value= IntVar()
        starting_population_entry = Entry(frame, textvariable=self.SP_value)
        starting_population_entry.grid(column=3, row=3, sticky=(W))
        SP_value = starting_population_entry.insert(0, 2000.0)
        #SP_value.set("20000")
        
        ## Gender Bias GB
        gender_bias_label = Label(frame, text="Gender Bias")
        gender_bias_label.grid(column=3, row=4, sticky=(W))
        self.GB_value= DoubleVar()
        gender_bias_entry = Entry(frame, textvariable=self.GB_value)
        gender_bias_entry.grid(column=3, row=5, sticky=(W))
        #Define gender bias # 0.01 to 0.49 female dominant, 0.51 - 0.99 male dominant
        GB_value = gender_bias_entry.insert(2, 45)

        ## Gender other GO
        gender_other_label = Label(frame, text="Gender Other")
        gender_other_label.grid(column=3, row=6, sticky=(W))
        self.GO_value= DoubleVar()
        gender_other_entry = Entry(frame, textvariable=self.GO_value)
        gender_other_entry.grid(column=3, row=7, sticky=(W))
        GO_value = gender_other_entry.insert(3, 1)
        
        ## Occupation inheritance value OIV
        occupation_inheritance_value_label = Label(frame, text="Occupation Inheritance Value")
        occupation_inheritance_value_label.grid(column=3, row=8, sticky=(W))
        self.OIV_value= IntVar()
        occupation_inheritance_value_entry = Entry(frame, textvariable=self.OIV_value)
        occupation_inheritance_value_entry.grid(column=3, row=9, sticky=(W))
        OIV_value = occupation_inheritance_value_entry.insert(0, 25.0)
        
        ## Number of generations NOG
        number_of_generations_label = Label(frame, text="Number of Generations")
        number_of_generations_label.grid(column=3, row=10, sticky=(W))
        self.NOG_value= IntVar()
        number_of_generations_entry = Entry(frame, textvariable=self.NOG_value)
        number_of_generations_entry.grid(column=3, row=11, sticky=(W))
        NOG_value = number_of_generations_entry.insert(0, 3.0)
        
    def import_libraries(self):
        print('Importing libraries...')
        from datetime import datetime
        import pandas as pd
        import numpy as np
        import random

        import matplotlib.pyplot as plt
        get_ipython().run_line_magic('matplotlib', 'inline')

        print('Libraries imported!')
        
        global datetime
        global pd
        global np
        global random
        global plt
    
    def load_database(self):
    
        Windows_version = self.OS_selected_value.get() #Run excel datafile on Windows  =1, or MacOS =0 (edited excel version for better usability)
        
        global xls
        global xls2
        global xls3
        
        print('Loading database...')
        print('Data sources: Employment Projections program, U.S. Bureau of Labor Statistics')
        print('Data sources: data.world US Census Bureau')
        #Sources: Employment Projections program, U.S. Bureau of Labor Statistics
        #https://data.world/uscensusbureau/frequently-occurring-surnames-from-the-census-2010
        # same source for first and last names
        #for Windows 
        if Windows_version ==1:
            xls = pd.ExcelFile(r'C:\Users\Nasim\Desktop\Evolution_game_project\occupation_canedit.xlsx')
            xls2 = pd.ExcelFile(r'C:\Users\Nasim\Desktop\Evolution_game_project\firstnames_edited.xlsx')
            xls3 = pd.ExcelFile(r'C:\Users\Nasim\Desktop\Evolution_game_project\lastnames_edited.xlsx')
        else:
            #for Mac
            xls = pd.ExcelFile(r'/Users/nasimnassar/Desktop/OccupyEvolution/occupation_canedit.xlsx')
            xls2 = pd.ExcelFile(r'/Users/nasimnassar/Desktop/OccupyEvolution/firstnames_edited.xlsx')
            xls3 = pd.ExcelFile(r'/Users/nasimnassar/Desktop/OccupyEvolution/lastnames_edited.xlsx')
    
        print('Databases loaded!')
        
        global df1
        global df_firstnames
        global df_lastnames
        
        print('Creating dataframes...')
        #Load sheets as dataframes
        df1 = pd.read_excel(xls, 'Table 1.2') #Main Database
        #df2 = pd.read_excel(xls, 'Table 1.3')
        df_firstnames = pd.read_excel(xls2, 'Blatt 1 - babynames-clean')
        df_lastnames = pd.read_excel(xls3, 'Blatt 1 - Names_2010Census')
        
        global Occupation_2019
        global Employment_titles
        global reduced_Employment_titles_topcategories
        global probability_for_top_category
        global Occupation_code_topcategories_index
        global Occupation_percent_2019_new
        global Occupation_name_lineitems_index
        global reduced_Occupation_2019_numbers_top

        #First and Last Names
        fn_all = df_firstnames['Name'].tolist()
        fn_males = df_firstnames['Name'].loc[df_firstnames['Gender'] == 'boy'].tolist()
        fn_females = df_firstnames['Name'].loc[df_firstnames['Gender'] == 'girl'].tolist()
        last_names = df_lastnames['name'].tolist()
        print('Dataframes created!')

        #Headers #Columns
        Occupation_titles = df1['2019 National Employment Matrix title'].tolist()
        Occupation_code = df1['2019 National Employment Matrix code'].tolist()
        Occupation_type = df1['Occupation type'].tolist()
        Occupation_2019 = df1['Employment, 2019'].tolist()
        Occupation_2029 = df1['Employment, 2029'].tolist()
        Occupation_percent_2019 = df1['Employment distribution, percent, 2019'].tolist()
        Occupation_percent_2029 = df1['Employment distribution, percent, 2029'].tolist()
        Occupation_change_numeric = df1['Employment change, numeric, 2019-29'].tolist()
        Occupation_change_percent = df1['Employment change, percent, 2019-29'].tolist()
        Occupation_annual_average = df1['Occupational openings, 2019-29 annual average'].tolist()

        #Edit headers into usable strings
        Employment_titles = [0]*len(Occupation_titles)
        count = 0        
        for i in range(len(Occupation_titles)):
            count += 1
            Employment_titles_temp = Occupation_titles[count-1].replace(' ', '_')
            Employment_titles_temp2 = Employment_titles_temp.replace(',', '')
            Employment_titles[count-1] = Employment_titles_temp2

        #Add additional strings "_all" & "_sum"
        Employment_titles_all = [0]*len(Employment_titles)
        Employment_titles_sum = [0]*len(Employment_titles)
        count = 0
        for i in range(len(Employment_titles)):
            count += 1
            Employment_titles_all[count-1] = Employment_titles[count-1] + '_all'
            Employment_titles_sum[count-1] = Employment_titles[count-1] + '_sum'

        #Define top and subcategories
        # Occupation (all) top and sub-categories (Summary vs Line item) and index
        Occupation_code_allcategories = df1['2019 National Employment Matrix code'].loc[df1['Occupation type'] == 'Summary']
        Occupation_code_allcategories_index = Occupation_code_allcategories.index
        # Occupation code top categories and index
        Occupation_code_topcategories = df1[df1['2019 National Employment Matrix code'].str.contains('-0000', regex=False)]
        Occupation_code_topcategories_index = Occupation_code_topcategories.index
        # Line item occupations and index
        Occupation_code_lineitems = df1.loc[df1['Occupation type'] == 'Line item']
        Occupation_code_lineitems_index = Occupation_code_lineitems.index
        # Line item occupation numbers and index
        Occupation_name_lineitems = df1['Employment, 2019'].loc[df1['Occupation type'] == 'Line item']
        Occupation_name_lineitems_index = Occupation_name_lineitems.index

        #Empty lists
        Matrix_code_topcategories = [0]*len(Employment_titles)
        Matrix_code_subcategories = [0]*len(Employment_titles)
        Matrix_code_lineitems = [0]*len(Employment_titles)
        Matrix_code_subsubcategories = [0]*len(Employment_titles)

        Employment_titles_topcategories = [0]*len(Employment_titles)
        Employment_titles_subcategories = [0]*len(Employment_titles)
        Employment_titles_lineitems = [0]*len(Employment_titles)
        Employment_titles_subsubcategories = [0]*len(Employment_titles)

        Occupation_2019_numbers_top = [0]*len(Employment_titles)
        Occupation_2019_numbers_sub = [0]*len(Employment_titles)
        Occupation_2019_numbers_lineitem = [0]*len(Employment_titles)
        Occupation_2019_numbers_subsub = [0]*len(Employment_titles)

        #Separate top and subcategories from actual employment titles #It works but 2nd and 3rd level are not a great separation
        count = 0
        for i in range(len(Employment_titles)):
            count += 1
            # separate "Summary" from "Line item"
            if i in Occupation_code_allcategories_index:
                #Separate top categories from sub categories (1st level)
                if str('-0000') in Occupation_code[i]:
                    Matrix_code_topcategories[i] = Occupation_code[i]
                    Employment_titles_topcategories[i] = Employment_titles[i]
                    Occupation_2019_numbers_top[i] = Occupation_2019[i]
                else:
                    if str('000') in Occupation_code[i]:
                        # if separate sub (2nd level) from subsub (3rd level category) 
                        Matrix_code_subcategories[i] = Occupation_code[i]
                        Employment_titles_subcategories[i] = Employment_titles[i]
                        Occupation_2019_numbers_sub[i] = Occupation_2019[i]
                    else:
                        Matrix_code_subsubcategories[i] = Occupation_code[i]
                        Employment_titles_subsubcategories[i] = Employment_titles[i]
                        Occupation_2019_numbers_subsub[i] = Occupation_2019[i]
            # if "Line item" (4th level)
            else:
                Matrix_code_lineitems[i] = Occupation_code[i]
                Employment_titles_lineitems[i] = Employment_titles[i]
                Occupation_2019_numbers_lineitem[i] = Occupation_2019[i]

        #New precentages
        Occupation_percent_2019_new = [0]*len(Occupation_percent_2019)
        Occupation_percent_2029_new = [0]*len(Occupation_percent_2029)
        for i in range(len(Occupation_percent_2019)):
            Occupation_percent_2019_new[i] = (Occupation_2019[i]/Occupation_2019[0])*100
            Occupation_percent_2029_new[i] = (Occupation_2029[i]/Occupation_2029[0])*100


        #Probability of being in any top category
        reduced_Employment_titles_topcategories = [i for i in Employment_titles_topcategories if i != 0]
        reduced_Occupation_2019_numbers_top = [i for i in Occupation_2019_numbers_top if i != 0]
        
        del reduced_Employment_titles_topcategories[0]
        del reduced_Occupation_2019_numbers_top[0]

        reduced_Employment_titles_topcategories = reduced_Employment_titles_topcategories
        reduced_Occupation_2019_numbers_top = reduced_Occupation_2019_numbers_top

        probability_for_top_category = [0]*len(Occupation_code_topcategories_index)
        count=0
        for i in Occupation_code_topcategories_index:
            count +=1
            probability_for_top_category[count-1] = Occupation_percent_2019_new[i]
        del probability_for_top_category[0]

        print('Occupations defined')
        
    #############################    
    def create_starting_population(self):
        #Create society
        
        display_demographic_figures = self.DDF_selected_value.get()
        occupation_inheritance = self.OI_selected_value.get()
        display_real_data_percentages = self.DRDP_selected_value.get() # Error in bar plot!
        display_population_data = self.DPD_selected_value.get()
        
        global population_df
        global lower_boundary_topcategory
        global upper_boundary_topcategory
        global gender_sizes
        global gender
        global gender_labels
        global gender_distribution_female
        global gender_distribution_male
        global gender_other
        global fn_all
        global fn_males
        global fn_females
        global weights_fn_males
        global weights_fn_females
        global weights_fn_all
        global reduced_Employment_titles_topcategories
        global probability_for_top_category
        global reduced_Occupation_2019_numbers_top
        global Occupation_2019
        global Employment_titles
        global Occupation_code_topcategories_index
        global Occupation_percent_2019_new
        global Occupation_name_lineitems_index
        
        population_size = self.SP_value.get() # 1 million takes a little over 4 minutes to generate population
        gender_bias = self.GB_value.get()
        gender_other = self.GO_value.get()
    
        #Progress timers
        start_time = datetime.now() #Timer start
        timer_percentages_interval_5s = np.arange(0.05,1.05,0.05)
        timer_percentages_5s = [int(round(i * population_size, 0)) for i in timer_percentages_interval_5s]
        timer_percentages_interval_10s = np.arange(0.1,1.1,0.1)
        timer_percentages_10s = [int(round(i * population_size, 0)) for i in timer_percentages_interval_10s]

        #First and Last Names
        fn_all = df_firstnames['Name'].tolist()
        fn_males = df_firstnames['Name'].loc[df_firstnames['Gender'] == 'boy'].tolist()
        fn_females = df_firstnames['Name'].loc[df_firstnames['Gender'] == 'girl'].tolist()
        last_names = df_lastnames['name'].tolist()
    
        print('Creating a society...')
        print('Depending on population size, it may take a while longer')

        #Define population size
        print('You chose a population of ' + str(population_size) + ' Occupiers!')
        print('Population count = ' + str(population_size))

        #Define genders 
        gender = ('Male', 'Female', 'Other')

        #Distributions
        gender_distribution_male = (1 - gender_other)*gender_bias
        gender_distribution_female = (1 - gender_other)*(1-gender_bias)
        print(gender_bias, gender_other)

        if gender_distribution_female + gender_distribution_male + gender_other ==1:
            print('Total gender distribution equals 100%')
        else:
            if abs(1-(gender_distribution_female + gender_distribution_male + gender_other)) < 0.0001:
                print('Error pass: Total gender distribution almost equals 100%')
            else:
                print('Gender distribution error!')
        
        #create individuals with genders
        print('Assigning random genders to occupiers...')
        population_gender = random.choices(population=gender,
                                           weights=[gender_distribution_male, 
                                                    gender_distribution_female, 
                                                    gender_other],
                                           k=population_size)
        population_df = pd.DataFrame(population_gender)

        #Create Names
        print('Creating names...')
        first_name=[0]*population_size
        weights_fn_males = [1/len(fn_males)]*len(fn_males)
        weights_fn_females = [1/len(fn_females)]*len(fn_females)
        weights_fn_all = [1/len(fn_all)]*len(fn_all)

        last_name=[0]*population_size
        weights_last_names = [1/len(last_name)]*len(last_names)
        count=0
        for i in range(len(population_gender)):
            count += 1
            if count in timer_percentages_10s:
                if count == timer_percentages_10s[0]:
                    print('10%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_percentages_10s[1]:
                    print('20%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_percentages_10s[2]:
                    print('30%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_percentages_10s[3]:
                    print('40%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_percentages_10s[4]:
                    print('50%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_percentages_10s[5]:
                    print('60%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_percentages_10s[6]:
                    print('70%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_percentages_10s[7]:
                    print('80%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_percentages_10s[8]:
                    print('90%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_percentages_10s[9]:
                    print('100%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
        
            if population_gender[i] == 'Male':
                first_name[count-1] = random.choices(population=fn_males,weights=weights_fn_males,k=1)
                last_name[count-1] = random.choices(population=last_names,weights=weights_last_names,k=1)
            elif population_gender[i] == 'Female':
                first_name[count-1] = random.choices(population=fn_females,weights=weights_fn_females,k=1)
                last_name[count-1] = random.choices(population=last_names,weights=weights_last_names,k=1)
            elif population_gender[i] == 'Other':
                first_name[count-1] = random.choices(population=fn_all,weights=weights_fn_all,k=1)
                last_name[count-1] = random.choices(population=last_names,weights=weights_last_names,k=1)

            if last_name[count-1] == 'NASSAR':
                print('Nassar in the house!!!!!!!!!!!!')
                print('I repeat, Nassar in the house!')

        #Create individual occupation
        print('Creating jobs...')
        #Assign top category
        individual_occupation_top_category = random.choices(population=reduced_Employment_titles_topcategories,
                                                            weights=probability_for_top_category,
                                                            k=population_size)

        print('Creating jobs is easy!')

        population_df = pd.DataFrame(list(zip(population_gender, individual_occupation_top_category)),columns =['Gender', 'top category'])

        #Assign sub category
        print('Creating specific occupations...')
        lower_boundary_topcategory = [0]*population_size
        upper_boundary_topcategory = [len(Employment_titles)]*population_size
        individual_occupation_sub_category = [0]*population_size
        #individual_occupation_sub_category
        count = 0
        for i in individual_occupation_top_category:
            count += 1
            #Where top category starts
            lower_boundary_topcategory[count-1] = Employment_titles.index(i)
            #Where top category ends
            for ii in Occupation_code_topcategories_index:
                if ii > lower_boundary_topcategory[count-1]:
                    upper_boundary_topcategory[count-1] = ii
                    probability_for_sub_category = Occupation_percent_2019_new[lower_boundary_topcategory[count-1]+1:
                                                                               upper_boundary_topcategory[count-1]-1]
                    temp2 = [x for x in Occupation_name_lineitems_index if lower_boundary_topcategory[count-1] <= x <= upper_boundary_topcategory[count-1]]
                    Number_employments_2019_subcategory = [0]*len(temp2)
                    individual_occupation_sub_categories = [0]*len(temp2)
                    count2=0
                    for i in temp2:
                        count2 += 1
                        Number_employments_2019_subcategory[count2-1] = Occupation_2019[i]
                        individual_occupation_sub_categories[count2-1] = Employment_titles[i]
            
                    probability_for_sub_category_new = [x / Occupation_2019[lower_boundary_topcategory[count-1]] for x in Number_employments_2019_subcategory]
            
                    individual_occupation_sub_category[count-1] = random.choices(population=individual_occupation_sub_categories,
                                                                                 weights=probability_for_sub_category_new,
                                                                                 k=1)
                    break
                if ii == max(Occupation_code_topcategories_index):
                    upper_boundary_topcategory[count-1] = len(Employment_titles)
                    probability_for_sub_category = Occupation_percent_2019_new[lower_boundary_topcategory[count-1]+1:
                                                                               upper_boundary_topcategory[count-1]-1]
                    temp2 = [x for x in Occupation_name_lineitems_index if lower_boundary_topcategory[count-1] <= x <= upper_boundary_topcategory[count-1]]
                    Number_employments_2019_subcategory = [0]*len(temp2)
                    individual_occupation_sub_categories = [0]*len(temp2)
                    count2=0
                    for i in temp2:
                        count2 += 1
                        Number_employments_2019_subcategory[count2-1] = Occupation_2019[i]
                        individual_occupation_sub_categories[count2-1] = Employment_titles[i]
                
                    probability_for_sub_category_new = [x / Occupation_2019[lower_boundary_topcategory[count-1]] for x in Number_employments_2019_subcategory]
            
                    individual_occupation_sub_category[count-1] = random.choices(population=individual_occupation_sub_categories,
                                                                                 weights=probability_for_sub_category_new,
                                                                                 k=1)
    
                    break
            else:
                continue

        print('This one was a bit trickier!')    

        #Assign Generation Age and category 
        #0=Generation Zero, 1=First babies,  2=First babies are Adults, and so on...
        generation_age = [0]*population_size #Generation Zero
        age_category = [1]*population_size  #0=Baby, 1=Adult (can have babies), 2=Other #Generation Zero already adults

        #Assign each individual a random number
        individual_random_number = [0]*population_size
        count = 0
        for i in range(population_size):
            count += 1
            individual_random_number[count-1] = np.random.normal(0,1)

        population_df = pd.DataFrame(list(zip(population_gender,first_name,last_name,generation_age,age_category,individual_occupation_top_category,individual_occupation_sub_category,individual_random_number)),columns =['Gender', 'First Name', 'Last Name', 'Generation Age','Age category', 'Top category', 'Sub category','Ind Random Number'])

        print('Starting population created!')
        #pd.set_option('display.max_rows', None)
        #pd.set_option('display.max_columns', None)
        #pd.set_option('display.width', 1000)
        #print(population_df)
        gender_labels = gender
        gender_sizes = np.array([len(population_df[population_df['Gender'] == 'Male'])/population_size,
                                 len(population_df[population_df['Gender'] == 'Female'])/population_size,
                                 len(population_df[population_df['Gender'] == 'Other'])/population_size])
    
    
        writer = pd.ExcelWriter(r'/Users/nasimnassar/Desktop/OccupyEvolution/Starting_Population.xlsx', engine = 'xlsxwriter')
        population_df.to_excel(writer, sheet_name ='Generation Zero') #, index = False)
        writer.save()
        #writer.close()
        
        #Plotting figures of demographics    
        #Figures
        if display_demographic_figures == 1:
            print('Displaying generation 0001...')
            print('Creating pie charts...')
            fig, ax4 = plt.subplots(figsize=(10,10))

            plt.title("Population Demographics Gen Zero - Gender")
            gender_labels = gender
            gender_sizes = np.array([len(population_df[population_df['Gender'] == 'Male'])/len(population_df),
                                     len(population_df[population_df['Gender'] == 'Female'])/len(population_df),
                                     len(population_df[population_df['Gender'] == 'Other'])/len(population_df)])
            explode = np.zeros(len(gender_sizes))
            explode[gender_sizes.argmax()] = 0.1
            ax4.pie(gender_sizes, explode=explode, labels=gender_labels, autopct='%1.1f%%', shadow=True, startangle=20)
            ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()

            #Figure2
            fig, ax5 = plt.subplots(figsize=(10,10))
            
            plt.title("Population Demographics Gen Zero - Occupation category")
            top_category_labels = population_df['Top category'].unique()
        
            top_category_counts = population_df["Top category"].value_counts()
            ###
            #Sort labels like standard reduced_Employment_titles_topcategories
            synth_top_category_count = [0]*len(reduced_Employment_titles_topcategories)
            synth_top_category_percent = [0]*len(reduced_Employment_titles_topcategories)
            count = 0
            for i in reduced_Employment_titles_topcategories: #range(len(population_df)):
                count +=1
                synth_top_category_count[count-1] = len(population_df.loc[population_df['Top category'] == i])
                synth_top_category_percent[count-1] = (synth_top_category_count[count-1] / len(population_df)) * 100

            explode2 = np.zeros(len(synth_top_category_count))
            explode2[np.argmax(synth_top_category_count)] = 0.1
            ax5.pie(synth_top_category_count, explode=explode2, labels=reduced_Employment_titles_topcategories, autopct='%1.1f%%', shadow=True, startangle=90)
            ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()
            print('Pie charts created')
        
        #Display population data
        if display_population_data == 1:
            print('Displaying your minion data...')
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            print(population_df)
        
    
    #############################    
    def create_first_generation(self):
        
        display_demographic_figures = self.DDF_selected_value.get()
        occupation_inheritance = self.OI_selected_value.get()
        display_real_data_percentages = self.DRDP_selected_value.get() # Error in bar plot!
        display_population_data = self.DPD_selected_value.get()
        
        start_time = datetime.now() #Timer start
        
        global lower_boundary_topcategory
        global upper_boundary_topcategory
        global gender_sizes
        global gender
        global gender_labels
        global gender_distribution_female
        global gender_distribution_male
        global gender_other
        global fn_all
        global fn_males
        global fn_females
        global weights_fn_males
        global weights_fn_females
        global weights_fn_all
        global reduced_Employment_titles_topcategories
        global probability_for_top_category
        global reduced_Occupation_2019_numbers_top
        global Occupation_2019
        global Employment_titles
        global Occupation_code_topcategories_index
        global Occupation_percent_2019_new
        global Occupation_name_lineitems_index
        
        occupation_inheritance_value = self.OIV_value.get()
        gender_bias = self.GB_value.get()
        gender_other = self.GO_value.get()
        
        start_time = datetime.now() #Timer start
        print('Time: {}'.format(start_time))
        
        xls_start_population = pd.ExcelFile(r'/Users/nasimnassar/Desktop/OccupyEvolution/Starting_Population.xlsx')
       
        population_df = pd.read_excel(xls_start_population, 'Generation Zero')
                
        gender_labels = gender
        gender_sizes = np.array([len(population_df[population_df['Gender'] == 'Male'])/len(population_df),
                                 len(population_df[population_df['Gender'] == 'Female'])/len(population_df),
                                 len(population_df[population_df['Gender'] == 'Other'])/len(population_df)])
    
        mean_time = datetime.now() #Timer end
        print('Duration: {}'.format(mean_time - start_time))
        print('Start Generation 0001')
        
        #create first generation
        #Determine how many couples can be produced
        if gender_sizes[0] > gender_sizes[1]:
            secondhighest_gender_size =  gender_sizes[1]
            secondhighest_gender_label =  gender_labels[1]
            couples = len(population_df[population_df['Gender'] == 'Female'])
        elif gender_sizes[0] == gender_sizes[1]:
            secondhighest_gender_size =  gender_sizes[1]
            secondhighest_gender_label =  gender_labels[1]
            couples = len(population_df[population_df['Gender'] == 'Female'])
        elif gender_sizes[0] < gender_sizes[1]:
            secondhighest_gender_size =  gender_sizes[0]
            secondhighest_gender_label =  gender_labels[0]
            couples = len(population_df[population_df['Gender'] == 'Male'])
        
        print('Generation Zero Couples:',couples)
        
        #Progress timers
        timer_percentages_interval_5s = np.arange(0.05,1.05,0.05)
        timer_percentages_5s = [int(round(i * couples, 0)) for i in timer_percentages_interval_5s]
        timer_percentages_interval_10s = np.arange(0.1,1.1,0.1)
        timer_percentages_10s = [int(round(i * couples, 0)) for i in timer_percentages_interval_10s]

        timer_couples_percentages_10s = [int(round(i * couples, 0)) for i in timer_percentages_interval_10s]
    
        #timer
        mean_time = datetime.now() #Timer end
        print('Duration: {}'.format(mean_time - start_time))
        #Create next generation
        print('Creating a new generation of occupiers...')
        if occupation_inheritance ==1:
            print('creating inherited jobs...')
        else:
            print('creating random jobs...')
        
        male_parents_gen_0000 = [0]*couples
        female_parents_gen_0000 =[0]*couples

        population_gen_0001temp2 = [0]*couples
        
        count = 0
        count_number_of_children = 0
        print('Couples getting busy making new occupiers...')
        for i in range(couples):
            #print(i)
            count += 1
            if count in timer_couples_percentages_10s:
                if count == timer_couples_percentages_10s[0]:
                    print('10%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_couples_percentages_10s[1]:
                    print('20%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_couples_percentages_10s[2]:
                    print('30%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_couples_percentages_10s[3]:
                    print('40%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_couples_percentages_10s[4]:
                    print('50%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_couples_percentages_10s[5]:
                    print('60%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_couples_percentages_10s[6]:
                    print('70%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_couples_percentages_10s[7]:
                    print('80%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_couples_percentages_10s[8]:
                    print('90%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
                if count == timer_couples_percentages_10s[9]:
                    print('100%...')
                    mean_time = datetime.now() #Timer end
                    print('Duration: {}'.format(mean_time - start_time))
    
            male_parents_gen_0000[i] = population_df[population_df['Gender'] == 'Male'].sort_values('Ind Random Number').index[i]
            female_parents_gen_0000[i] = population_df[population_df['Gender'] == 'Female'].sort_values('Ind Random Number').index[i]
    
            parents_gen_0000 = pd.concat([population_df.iloc[[population_df[population_df['Gender'] == 'Male'].sort_values('Ind Random Number').index[i]]],
                                          population_df.iloc[[population_df[population_df['Gender'] == 'Female'].sort_values('Ind Random Number').index[i]]]])
            #Number of children for each couple 0-5, 2 is most common, then 1 and 3, then 4, then 0 and 5
            number_of_children = int(np.random.choice(8, 1, p=[0, 0.2, 0.4, 0.2, 0.1, 0.05, 0.025, 0.025]))
            gen_0001_gender = [0]
        
            count_number_of_children += number_of_children
    
            count2=0
            population_gen_0001temp = [0]*number_of_children
            for ii in range(number_of_children):
                count2 += 1
                #Gender
                gen_0001_gender = random.choices(population=gender_labels,
                                                 weights=[gender_distribution_male,gender_distribution_female,gender_other],
                                                 k=1)
                #Individual random number
                individual_random_number = [np.random.normal(0,1)]
                #Names
                #print(i, population_df_orig['Last Name'][i])
                if gen_0001_gender == ['Male']:
                    first_name = random.choices(population=fn_males,weights=weights_fn_males,k=1)
                    last_name = population_df['Last Name'][i]
                elif gen_0001_gender == ['Female']:
                    first_name = random.choices(population=fn_females,weights=weights_fn_females,k=1)
                    last_name = population_df['Last Name'][i]
                elif gen_0001_gender == ['Other']:
                    first_name = random.choices(population=fn_all,weights=weights_fn_all,k=1)
                    last_name = population_df['Last Name'][i]
                
                new_last_name = [0]
                new_last_name[0] = last_name
                #del last_name
                #print(new_last_name[0])
                
                #Assign top category
                if occupation_inheritance == 0:
                    individual_occupation_top_category = random.choices(population=reduced_Employment_titles_topcategories,
                                                                        weights=probability_for_top_category,
                                                                        k=1)
                elif occupation_inheritance ==1:
                    #boosted_probability

                    probability_for_top_category_temp = [0]*len(probability_for_top_category)
                    #Find parents occupations
                    count3=0
                    for iii in reduced_Employment_titles_topcategories:
                        count3+=1
                        fathers_occupation = parents_gen_0000['Top category'].loc[parents_gen_0000['Gender'] == 'Male'].tolist()
                        mothers_occupation = parents_gen_0000['Top category'].loc[parents_gen_0000['Gender'] == 'Female'].tolist()

                        if iii == fathers_occupation[0] and iii == mothers_occupation[0]:
                            fathers_occupation_index = iii
                            fathers_occupation_total = reduced_Occupation_2019_numbers_top[count3-1]
                            mothers_occupation_index = iii
                            mothers_occupation_total = 0
                
                        elif iii == fathers_occupation[0]:
                            fathers_occupation_index = iii
                            fathers_occupation_total = reduced_Occupation_2019_numbers_top[count3-1]

                        elif iii == mothers_occupation[0]:
                            mothers_occupation_index = iii
                            mothers_occupation_total = reduced_Occupation_2019_numbers_top[count3-1]
                        else:
                            dfsdf= 432
                            #New probability weights for top category
                    count4=0
                    for iiii in reduced_Employment_titles_topcategories:
                        count4+=1
                        if iiii == fathers_occupation[0] and iiii == mothers_occupation[0]:
                            probability_for_top_category_temp[count4-1] = occupation_inheritance_value
            
                        elif iiii == fathers_occupation[0]:
                            probability_for_top_category_temp[count4-1] = occupation_inheritance_value
                        elif iiii == mothers_occupation[0]:
                            probability_for_top_category_temp[count4-1] = occupation_inheritance_value
                        else:
                            probability_for_top_category_temp[count4-1] = (reduced_Occupation_2019_numbers_top[count4-1] / (Occupation_2019[0] - fathers_occupation_total - mothers_occupation_total)) * (2*occupation_inheritance_value)
        
                #Choose top category
                individual_occupation_top_category_temp = random.choices(population=reduced_Employment_titles_topcategories,
                                                                         weights=probability_for_top_category_temp,
                                                                         k=1)
        
                #Choose subcategory depending on top category
                count5=0
                for iiiii in Occupation_code_topcategories_index:
                    count5+=1
                    if Employment_titles[iiiii] == individual_occupation_top_category_temp[0]:
                        lower_boundary_temp = iiiii
                        if lower_boundary_temp == max(Occupation_code_topcategories_index):
                            upper_boundary_temp = len(Employment_titles)
                    
                        else:
                            upper_boundary_temp = Occupation_code_topcategories_index[count5]
                    
                        probability_for_sub_category_temp = Occupation_percent_2019_new[lower_boundary_temp+1:
                                                                                        upper_boundary_temp-1]
                        temp2 = [x for x in Occupation_name_lineitems_index 
                                 if lower_boundary_temp <= x <= upper_boundary_temp]
                        Number_employments_2019_subcategory = [0]*len(temp2)
                        individual_occupation_sub_categories_temp = [0]*len(temp2)
                        count6=0
                        for iiiiii in temp2:
                            count6 += 1
                            Number_employments_2019_subcategory[count6-1] = Occupation_2019[iiiiii]
                            individual_occupation_sub_categories_temp[count6-1] = Employment_titles[iiiiii]
                            #print(Number_employments_2019_subcategory)
            
                        probability_for_sub_category_new = [x / Occupation_2019[lower_boundary_temp] for x in Number_employments_2019_subcategory]
            
                        individual_occupation_sub_category_temp = random.choices(population=individual_occupation_sub_categories_temp,
                                                                                 weights=probability_for_sub_category_new,
                                                                                 k=1)
                    else:
                        #do nothing
                        fdgfgfsgfgsfggr=1
                        #print('I am doing nothing...')
        
                generation_age = [1]
                age_category = [0]
                gen_0001_df = pd.DataFrame(list(zip(gen_0001_gender,first_name,new_last_name,generation_age,age_category,individual_occupation_top_category_temp,individual_occupation_sub_category_temp,individual_random_number)),
                                                    columns =['Gender', 'First Name', 'Last Name', 'Generation Age','Age category', 'Top category', 'Sub category','Ind Random Number'])
                
                pd.set_option("display.max_rows", None, "display.max_columns", None)
                
                population_gen_0001temp[ii] = pd.DataFrame(gen_0001_df, columns =['Gender', 'First Name', 'Last Name', 'Generation Age','Age category', 'Top category', 'Sub category','Ind Random Number'])

            population_gen_0001temp2[i] = pd.concat(population_gen_0001temp)
            del population_gen_0001temp

        population_gen_0001temp3 = pd.DataFrame(columns =['Gender', 'First Name', 'Last Name', 'Generation Age','Age category', 'Top category', 'Sub category','Ind Random Number'])
        #print("population_gen_0001temp3:" , population_gen_0001temp3)
        
        population_gen_0001temp3 = pd.concat(population_gen_0001temp2)
        population_gen_0001 = population_gen_0001temp3
        population_gen_0001.index = range(len(population_gen_0001.index))
        print('Number of total children in generation 0001: ', count_number_of_children)

        #timer
        mean_time = datetime.now() #Timer end
        print('Duration: {}'.format(mean_time - start_time))

        
        #Plotting figures of demographics    
        #Figures
        if display_demographic_figures == 1:
            print('Displaying generation 0001...')
            print('Creating pie charts...')
            fig, ax4 = plt.subplots(figsize=(10,10))

            plt.title("Population Demographics Gen 0001 - Gender")
            gender_labels = gender
            gender_sizes = np.array([len(population_gen_0001[population_gen_0001['Gender'] == 'Male'])/count_number_of_children,
                                     len(population_gen_0001[population_gen_0001['Gender'] == 'Female'])/count_number_of_children,
                                     len(population_gen_0001[population_gen_0001['Gender'] == 'Other'])/count_number_of_children])
            explode = np.zeros(len(gender_sizes))
            explode[gender_sizes.argmax()] = 0.1
            ax4.pie(gender_sizes, explode=explode, labels=gender_labels, autopct='%1.1f%%', shadow=True, startangle=20)
            ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()

            #Figure2
            fig, ax5 = plt.subplots(figsize=(10,10))
            
            plt.title("Population Demographics Gen 0001 - Occupation category")
            top_category_labels = population_gen_0001['Top category'].unique()
        
            top_category_counts = population_gen_0001["Top category"].value_counts()
            ###
            #Sort labels like standard reduced_Employment_titles_topcategories
            synth_top_category_count = [0]*len(reduced_Employment_titles_topcategories)
            synth_top_category_percent = [0]*len(reduced_Employment_titles_topcategories)
            count = 0
            for i in reduced_Employment_titles_topcategories: #range(len(population_df)):
                count +=1
                synth_top_category_count[count-1] = len(population_gen_0001.loc[population_gen_0001['Top category'] == i])
                synth_top_category_percent[count-1] = (synth_top_category_count[count-1] / count_number_of_children) * 100

            explode2 = np.zeros(len(synth_top_category_count))
            explode2[np.argmax(synth_top_category_count)] = 0.1
            ax5.pie(synth_top_category_count, explode=explode2, labels=reduced_Employment_titles_topcategories, autopct='%1.1f%%', shadow=True, startangle=90)
            ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()
            print('Pie charts created')

        population_df_new = population_gen_0001
        
        #Display population data
        if display_population_data ==1:
            print('Displaying your minion data...')
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            print(population_df_new)
        
        writer = pd.ExcelWriter(r'/Users/nasimnassar/Desktop/OccupyEvolution/Generation_0001.xlsx', engine = 'xlsxwriter')
        population_df_new.to_excel(writer, sheet_name ='Generation 0001') #, index = False)
        writer.save()
    
    #################################
    def create_next_generation(self):
    
        occupation_inheritance_value = self.OIV_value.get()
        number_of_generations = self.NOG_value.get()
        
        display_demographic_figures = self.DDF_selected_value.get()
        occupation_inheritance = self.OI_selected_value.get()
        display_real_data_percentages = self.DRDP_selected_value.get() # Error in bar plot!
        display_population_data = self.DPD_selected_value.get()
    
        start_time = datetime.now() #Timer start
        print('Time: {}'.format(start_time))
    
        xls_start_population = pd.ExcelFile(r'/Users/nasimnassar/Desktop/OccupyEvolution/Starting_Population.xlsx')
       
        population_df = pd.read_excel(xls_start_population, 'Generation Zero')
        population_df_orig = population_df
    
        timer_percentages_interval_10s = np.arange(0.1,1.1,0.1)
    
        for i in range(int(number_of_generations)): # from 0 until number_of_generations - 1
        
            generation_number = i + 1
            print('Generation Number: ' , generation_number)
            if i == 0:
                gen_population_df = population_df_orig
            else:
                gen_population_df = population_df_new
                
            gender_labels = gender
            gender_sizes = np.array([len(gen_population_df[gen_population_df['Gender'] == 'Male'])/len(gen_population_df),
                                     len(gen_population_df[gen_population_df['Gender'] == 'Female'])/len(gen_population_df),
                                     len(gen_population_df[gen_population_df['Gender'] == 'Other'])/len(gen_population_df)])
    
            mean_time = datetime.now() #Timer end
            print('Duration: {}'.format(mean_time - start_time))
            #print('End First Part!')
            print('Start Generation 000' + str(generation_number))
            #create second generation
            #Determine how many couples can be produced
            if gender_sizes[0] > gender_sizes[1]:
                secondhighest_gender_size =  gender_sizes[1]
                secondhighest_gender_label =  gender_labels[1]
                couples = len(gen_population_df[gen_population_df['Gender'] == 'Female'])
            elif gender_sizes[0] == gender_sizes[1]:
                secondhighest_gender_size =  gender_sizes[1]
                secondhighest_gender_label =  gender_labels[1]
                couples = len(gen_population_df[gen_population_df['Gender'] == 'Female'])
            elif gender_sizes[0] < gender_sizes[1]:
                secondhighest_gender_size =  gender_sizes[0]
                secondhighest_gender_label =  gender_labels[0]
                couples = len(gen_population_df[gen_population_df['Gender'] == 'Male'])
        
            print('Generation ' + str(generation_number) + ' Couples:',couples)    

            timer_couples_percentages_10s = [int(round(i * couples, 0)) for i in timer_percentages_interval_10s]
    
            #timer
            mean_time = datetime.now() #Timer end
            print('Duration: {}'.format(mean_time - start_time))
            #Create next generation
            print('Creating a new generation of occupiers...')
            if occupation_inheritance ==1:
                print('creating inherited jobs...')
            else:
                print('creating random jobs...')
        
            male_parents_gen_0000 = [0]*couples #population_df[population_df['Gender'] == 'Male'].sort_values('Ind Random Number')
            female_parents_gen_0000 =[0]*couples #population_df[population_df['Gender'] == 'Female'].sort_values('Ind Random Number')

            population_gen_0001temp2 = [0]*couples

            count = 0
            count_number_of_children = 0
            print('Couples getting busy making new occupiers...')
            for i in range(couples):
                #print(i)
                count += 1
                if count in timer_couples_percentages_10s:
                    if count == timer_couples_percentages_10s[0]:
                        print('10%...')
                        mean_time = datetime.now() #Timer end
                        print('Duration: {}'.format(mean_time - start_time))
                    if count == timer_couples_percentages_10s[1]:
                        print('20%...')
                        mean_time = datetime.now() #Timer end
                        print('Duration: {}'.format(mean_time - start_time))
                    if count == timer_couples_percentages_10s[2]:
                        print('30%...')
                        mean_time = datetime.now() #Timer end
                        print('Duration: {}'.format(mean_time - start_time))
                    if count == timer_couples_percentages_10s[3]:
                        print('40%...')
                        mean_time = datetime.now() #Timer end
                        print('Duration: {}'.format(mean_time - start_time))
                    if count == timer_couples_percentages_10s[4]:
                        print('50%...')
                        mean_time = datetime.now() #Timer end
                        print('Duration: {}'.format(mean_time - start_time))
                    if count == timer_couples_percentages_10s[5]:
                        print('60%...')
                        mean_time = datetime.now() #Timer end
                        print('Duration: {}'.format(mean_time - start_time))
                    if count == timer_couples_percentages_10s[6]:
                        print('70%...')
                        mean_time = datetime.now() #Timer end
                        print('Duration: {}'.format(mean_time - start_time))
                    if count == timer_couples_percentages_10s[7]:
                        print('80%...')
                        mean_time = datetime.now() #Timer end
                        print('Duration: {}'.format(mean_time - start_time))
                    if count == timer_couples_percentages_10s[8]:
                        print('90%...')
                        mean_time = datetime.now() #Timer end
                        print('Duration: {}'.format(mean_time - start_time))
                    if count == timer_couples_percentages_10s[9]:
                        print('100%...')
                        mean_time = datetime.now() #Timer end
                        print('Duration: {}'.format(mean_time - start_time))
    
                male_parents_gen_0000[i] = gen_population_df[gen_population_df['Gender'] == 'Male'].sort_values('Ind Random Number').index[i]
                female_parents_gen_0000[i] = gen_population_df[gen_population_df['Gender'] == 'Female'].sort_values('Ind Random Number').index[i]
    
                parents_gen_0000 = pd.concat([gen_population_df.iloc[[gen_population_df[gen_population_df['Gender'] == 'Male'].sort_values('Ind Random Number').index[i]]],
                                              gen_population_df.iloc[[gen_population_df[gen_population_df['Gender'] == 'Female'].sort_values('Ind Random Number').index[i]]]])
                #Number of children for each couple 0-5, 2 is most common, then 1 and 3, then 4, then 0 and 5
                number_of_children = int(np.random.choice(8, 1, p=[0, 0.2, 0.4, 0.2, 0.1, 0.05, 0.025, 0.025]))
                gen_0001_gender = [0]
        
                count_number_of_children += number_of_children
    
                count2=0
                population_gen_0001temp = [0]*number_of_children
                for ii in range(number_of_children):
                    count2 += 1
                    #Gender
                    gen_0001_gender = random.choices(population=gender_labels,
                                                     weights=[gender_distribution_male,gender_distribution_female,gender_other],
                                                     k=1)
                    #Individual random number
                    individual_random_number = [np.random.normal(0,1)]
                    #Names
                    if generation_number == 1:
                        #print(i, population_df_orig['Last Name'][i])
                        if gen_0001_gender == ['Male']:
                            first_name = random.choices(population=fn_males,weights=weights_fn_males,k=1)
                            last_name = population_df_orig['Last Name'][i]
                        elif gen_0001_gender == ['Female']:
                            first_name = random.choices(population=fn_females,weights=weights_fn_females,k=1)
                            last_name = population_df_orig['Last Name'][i]
                        elif gen_0001_gender == ['Other']:
                            first_name = random.choices(population=fn_all,weights=weights_fn_all,k=1)
                            last_name = population_df_orig['Last Name'][i]
                        print(last_name)
                        
                    else:
                        #print(i, population_df_new['Last Name'][i])
                        if gen_0001_gender == ['Male']:
                            first_name = random.choices(population=fn_males,weights=weights_fn_males,k=1)
                            last_name = population_df_new['Last Name'][i]
                        elif gen_0001_gender == ['Female']:
                            first_name = random.choices(population=fn_females,weights=weights_fn_females,k=1)
                            last_name = population_df_new['Last Name'][i]
                        elif gen_0001_gender == ['Other']:
                            first_name = random.choices(population=fn_all,weights=weights_fn_all,k=1)
                            last_name = population_df_new['Last Name'][i]
                        print(last_name)
                    
                    #Assign top category
                    if occupation_inheritance == 0:
                        individual_occupation_top_category = random.choices(population=reduced_Employment_titles_topcategories,
                                                                            weights=probability_for_top_category,
                                                                            k=1)
                    elif occupation_inheritance ==1:
                        #boosted_probability

                        probability_for_top_category_temp = [0]*len(probability_for_top_category)
                        #Find parents occupations
                        count3=0
                        for iii in reduced_Employment_titles_topcategories:
                            count3+=1
                            fathers_occupation = parents_gen_0000['Top category'].loc[parents_gen_0000['Gender'] == 'Male'].tolist()
                            mothers_occupation = parents_gen_0000['Top category'].loc[parents_gen_0000['Gender'] == 'Female'].tolist()

                            if iii == fathers_occupation[0] and iii == mothers_occupation[0]:
                                fathers_occupation_index = iii
                                fathers_occupation_total = reduced_Occupation_2019_numbers_top[count3-1]
                                mothers_occupation_index = iii
                                mothers_occupation_total = 0
                
                            elif iii == fathers_occupation[0]:
                                fathers_occupation_index = iii
                                fathers_occupation_total = reduced_Occupation_2019_numbers_top[count3-1]

                            elif iii == mothers_occupation[0]:
                                mothers_occupation_index = iii
                                mothers_occupation_total = reduced_Occupation_2019_numbers_top[count3-1]
                            else:
                                dfsdf= 432
                                #New probability weights for top category
                        count4=0
                        for iiii in reduced_Employment_titles_topcategories:
                            count4+=1
                            if iiii == fathers_occupation[0] and iiii == mothers_occupation[0]:
                                probability_for_top_category_temp[count4-1] = occupation_inheritance_value
                
                            elif iiii == fathers_occupation[0]:
                                probability_for_top_category_temp[count4-1] = occupation_inheritance_value
                            elif iiii == mothers_occupation[0]:
                                probability_for_top_category_temp[count4-1] = occupation_inheritance_value
                            else:
                                probability_for_top_category_temp[count4-1] = (reduced_Occupation_2019_numbers_top[count4-1] / (Occupation_2019[0] - fathers_occupation_total - mothers_occupation_total)) * (2*occupation_inheritance_value)
        
                    #Choose top category
                    individual_occupation_top_category_temp = random.choices(population=reduced_Employment_titles_topcategories,
                                                                             weights=probability_for_top_category_temp,
                                                                             k=1)
        
                    #Choose subcategory depending on top category
                    count5=0
                    for iiiii in Occupation_code_topcategories_index:
                        count5+=1
                        if Employment_titles[iiiii] == individual_occupation_top_category_temp[0]:
                            lower_boundary_temp = iiiii
                            if lower_boundary_temp == max(Occupation_code_topcategories_index):
                                upper_boundary_temp = len(Employment_titles)
                    
                            else:
                                upper_boundary_temp = Occupation_code_topcategories_index[count5]
                    
                            probability_for_sub_category_temp = Occupation_percent_2019_new[lower_boundary_temp+1:
                                                                                        upper_boundary_temp-1]
                            temp2 = [x for x in Occupation_name_lineitems_index 
                                     if lower_boundary_temp <= x <= upper_boundary_temp]
                            Number_employments_2019_subcategory = [0]*len(temp2)
                            individual_occupation_sub_categories_temp = [0]*len(temp2)
                            count6=0
                            for iiiiii in temp2:
                                count6 += 1
                                Number_employments_2019_subcategory[count6-1] = Occupation_2019[iiiiii]
                                individual_occupation_sub_categories_temp[count6-1] = Employment_titles[iiiiii]
                                #print(Number_employments_2019_subcategory)
            
                            probability_for_sub_category_new = [x / Occupation_2019[lower_boundary_temp] for x in Number_employments_2019_subcategory]
            
                            individual_occupation_sub_category_temp = random.choices(population=individual_occupation_sub_categories_temp,
                                                                                     weights=probability_for_sub_category_new,
                                                                                     k=1)
                        else:
                            #do nothing
                            fdgfgfsgfgsfggr=1
                            #print('I am doing nothing...')
        
                    generation_age = [1]
                    age_category = [0]
                    gen_0001_df = pd.DataFrame(list(zip(gen_0001_gender,first_name,last_name,generation_age,age_category,individual_occupation_top_category_temp,individual_occupation_sub_category_temp,individual_random_number)),
                                                        columns =['Gender', 'First Name', 'Last Name', 'Generation Age','Age category', 'Top category', 'Sub category','Ind Random Number'])

                    population_gen_0001temp[ii] = pd.DataFrame(gen_0001_df, columns =['Gender', 'First Name', 'Last Name', 'Generation Age','Age category', 'Top category', 'Sub category','Ind Random Number'])

                population_gen_0001temp2[i] = pd.concat(population_gen_0001temp)
                del population_gen_0001temp

            population_gen_0001temp3 = pd.DataFrame(columns =['Gender', 'First Name', 'Last Name', 'Generation Age','Age category', 'Top category', 'Sub category','Ind Random Number'])

            population_gen_0001temp3 = pd.concat(population_gen_0001temp2)
            population_gen_0001 = population_gen_0001temp3
            population_gen_0001.index = range(len(population_gen_0001.index))
            print('Number of total children in generation 000' + str(generation_number) + ': ', count_number_of_children)

            #timer
            mean_time = datetime.now() #Timer end
            print('Duration: {}'.format(mean_time - start_time))

            print('Displaying generation 000' + str(generation_number) + '...')
            #Plotting figures of demographics    
            #Figures
            if display_demographic_figures == 1:
                print('Creating pie charts...')
                fig, ax4 = plt.subplots(figsize=(10,10))

                plt.title("Population Demographics Gen" + str(generation_number) +  " - Gender")
                gender_labels = gender
                gender_sizes = np.array([len(population_gen_0001[population_gen_0001['Gender'] == 'Male'])/count_number_of_children,
                                         len(population_gen_0001[population_gen_0001['Gender'] == 'Female'])/count_number_of_children,
                                         len(population_gen_0001[population_gen_0001['Gender'] == 'Other'])/count_number_of_children])
                explode = np.zeros(len(gender_sizes))
                explode[gender_sizes.argmax()] = 0.1
                ax4.pie(gender_sizes, explode=explode, labels=gender_labels, autopct='%1.1f%%', shadow=True, startangle=20)
                ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.show()

                #Figure2
                fig, ax5 = plt.subplots(figsize=(10,10))
            
                plt.title("Population Demographics Gen" + str(generation_number) +  " - Occupation category")
                top_category_labels = population_gen_0001['Top category'].unique()
        
                top_category_counts = population_gen_0001["Top category"].value_counts()
                ###
                #Sort labels like standard reduced_Employment_titles_topcategories
                synth_top_category_count = [0]*len(reduced_Employment_titles_topcategories)
                synth_top_category_percent = [0]*len(reduced_Employment_titles_topcategories)
                count = 0
                for i in reduced_Employment_titles_topcategories: #range(len(population_df)):
                    count +=1
                    synth_top_category_count[count-1] = len(population_gen_0001.loc[population_gen_0001['Top category'] == i])
                    synth_top_category_percent[count-1] = (synth_top_category_count[count-1] / count_number_of_children) * 100

                explode2 = np.zeros(len(synth_top_category_count))
                explode2[np.argmax(synth_top_category_count)] = 0.1
                ax5.pie(synth_top_category_count, explode=explode2, labels=reduced_Employment_titles_topcategories, autopct='%1.1f%%', shadow=True, startangle=90)
                ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.show()
                print('Pie charts created')

            #pd.options.display.max_rows = 999
            #population_gen_0001
            population_df_new = population_gen_0001
        
            if generation_number == 1:
                writer = pd.ExcelWriter(r'/Users/nasimnassar/Desktop/OccupyEvolution/Generation_0001.xlsx', engine = 'xlsxwriter')
                population_df_new.to_excel(writer, sheet_name ='Generation 0001') #, index = False)
                writer.save()
            elif generation_number == 2:
                writer = pd.ExcelWriter(r'/Users/nasimnassar/Desktop/OccupyEvolution/Generation_0002.xlsx', engine = 'xlsxwriter')
                population_df_new.to_excel(writer, sheet_name ='Generation 0002') #, index = False)
                writer.save()
            elif generation_number == 3:
                writer = pd.ExcelWriter(r'/Users/nasimnassar/Desktop/OccupyEvolution/Generation_0003.xlsx', engine = 'xlsxwriter')
                population_df_new.to_excel(writer, sheet_name ='Generation 0003') #, index = False)
                writer.save()
            elif generation_number == 4:
                writer = pd.ExcelWriter(r'/Users/nasimnassar/Desktop/OccupyEvolution/Generation_0004.xlsx', engine = 'xlsxwriter')
                population_df_new.to_excel(writer, sheet_name ='Generation 0004') #, index = False)
                writer.save()
            
            #population_df_new.to_excel(r'/Users/nasimnassar/Desktop/OccupyEvolution/Starting Population.xlsx', sheet_name='Generation 000' + str(generation_number) , index = False)
            #with pd.ExcelWriter('Starting_Population.xlsx',
                                #mode='a') as writer:  
                                #population_df_new.to_excel(writer, sheet_name='Generation 000' + str(generation_number))
        
            #writer = pd.ExcelWriter(r'/Users/nasimnassar/Desktop/OccupyEvolution/Starting Population.xlsx', engine = 'xlsxwriter')
            #population_df_new.to_excel(writer, sheet_name = 'Generation 000' + str(generation_number))
            #writer.save()
            print('End loop ' + str(generation_number))
        if generation_number == number_of_generations:
            writer.close()
        else:
            donothing = 44844


        
    #def create_widgets(self):
        
        
root = Tk()
OccupyEvolutionApp(root)
root.mainloop()