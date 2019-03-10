#!/usr/bin/env python

from selenium.webdriver.common.by import By

import Driver
import pages.sell.sell_review_page as sell_review
from pages.base_page import BasePage


class MechanicalConditionPage(BasePage):
    def __init__(self):
        super(MechanicalConditionPage, self).__init__()

        self.title = "Complete Your Appraisal"

        self.vehicle_run_choices = self.yes_no_choices_xpath

        self.mechanical_condition = self.averages_xpath

        self.active_warning_light_choices = self.yes_no_choices_xpath

        self.flood_or_fire_damage_choices = self.yes_no_notsure_choices_xpath

    # selenium wrappers for all field
    # VEHICLE_RUN CHOICES
    def get_vehicle_run_choice_tab(self, vehicle_run_choice):
        vehicle_runs_xpath = '//*[@id="container-page"]/div/main/div[6]/div[2]/section/form/div[1]/label[1]/div[1]/' + \
                             self.vehicle_run_choices[vehicle_run_choice]
        return Driver.Instance.find_element(By.XPATH, vehicle_runs_xpath)

    def click_vehicle_run_choice_tab(self, vehicle_run_choice="No"):
        self.get_vehicle_run_choice_tab(vehicle_run_choice).click()

    # MECHANICAL CONDITION
    def get_mechanical_condition_checkbox(self, mechanical_condition_type):
        mechanical_condition_xpath = '//*[@id="container-page"]/div/main/div[6]/div[2]/section/form/div[1]/div[1]/div/' + \
                                     self.mechanical_condition[mechanical_condition_type]
        return Driver.Instance.find_element(By.XPATH, mechanical_condition_xpath)

    def check_mechanical_condition_checkbox(self, mechanical_condition_type="Above Average"):
        self.get_mechanical_condition_checkbox(mechanical_condition_type).click()

    # ACTIVE_WARNING_LIGHT CHOICES
    def get_active_warning_light_choice_tab(self, active_warning_light_choice):
        active_warning_lights_xpath = '//*[@id="container-page"]/div/main/div[6]/div[2]/section/form/div[1]/div[2]/div/div[1]/' + \
                                      self.active_warning_light_choices[active_warning_light_choice]
        return Driver.Instance.find_element(By.XPATH, active_warning_lights_xpath)

    def click_active_warning_light_choice_tab(self, active_warning_light_choice="No"):
        self.get_active_warning_light_choice_tab(active_warning_light_choice).click()

    # FLOOD_OR_FIRE_DAMAGE CHOICES
    def get_flood_or_fire_damage_choice_tab(self, flood_or_fire_damage_choice):
        flood_or_fire_damages_xpath = '//*[@id="container-page"]/div/main/div[6]/div[2]/section/form/div[1]/div[2]/label/div[1]/' + \
                                      self.flood_or_fire_damage_choices[flood_or_fire_damage_choice]
        return Driver.Instance.find_element(By.XPATH, flood_or_fire_damages_xpath)

    def click_flood_or_fire_damage_choice_tab(self, flood_or_fire_damage_choice="Yes"):
        self.get_flood_or_fire_damage_choice_tab(flood_or_fire_damage_choice).click()

    # ANYTHING ELSE
    @staticmethod
    def get_anything_else_textfield():
        return Driver.Instance.find_element(By.XPATH,
                                            '//*[@id="container-page"]/div/main/div[6]/div[2]/section/form/div[1]/label[2]/textarea')

    def set_anything_else_textfield(self, anything_else_str="Mechanical Information Completed: 1FDAF56F03EB97783"):
        self.get_anything_else_textfield().send_keys(anything_else_str)

    # CONTINUE
    def continue_button(self):
        self.click_continue_button()
        return sell_review.SellReview()
