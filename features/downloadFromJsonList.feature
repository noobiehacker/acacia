Feature: Reading a collection of youtubeLink and downloading it

  Scenario: A collection of youtubeLink is loaded into memory
  Given A collection of youtubeLink is loaded into memory
   When Youtube DL Library is called 1
   Then It will download link's file onto disk

#Test and Write a function that takes a collection of youtubeLink
#And run a for loop in each of them and download them one by one
