# -- FILE: features/example.feature
Feature: Parsing Json

  Scenario: Json is loaded from Disk or Web
    Given Function is called
     When Json is loaded 5
     Then It will be parsed and loaded in memory