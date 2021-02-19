# Pseudocode to experimental protocol
# see toolbox architecture in .drawio file

# open GUI choice: [new trial, lab report, subject IDs]

# start new trial --> pop up window asking for subject id

# display id foto of subject to check OK
  # access database
  # display picture
  # OK - Cancel

# display last progress of subject
  # access metadata
  # generate short history

# assigne upcoming trial
  # access experimental protocol
  # check group assigned to subject
  # check progress assigned to subject
  # assign next trial
  
# display setup instructions for pecking key positions
  # access experimental protocol
  # access upcoming trial information
  # display instructions for pecking key positions
  # display checklist before start

# display start - settings option
  
# Display instructions to place subject in start position and press OK

# display Timer for habituation phase

# start timer

# start video

# display start signal to release subject
## subject starts navigating maze

# start pecking key LED setting
  # access experimental protocol 
  # access upcoming trial information
  # control LEDs 

# wait for subject coice
  # waiting for pecking key feedback

# capture timestamp of pecking key

# evaluate choice and reward 

# stop reward

# stop timer

# stop video

# display intructions to catch subject

# update metadata 

# store video

# display trial report

# display instructions to repeat loop

# display instructions to end experiment

# display report of session

# end program 




