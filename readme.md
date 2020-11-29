CSV Should be in this format:
Run 1: Time (s),Run 1: Position (m),Run 1: Velocity (m/s),Run 1: Acceleration (m/s^2)
0.000000,0.182990,0.080986,-0.970732
0.050000,0.188822,0.033347,-0.916959
0.100000,0.188993,-0.021838,-0.711884
0.150000,0.185392,-0.055452,-0.231430
0.200000,0.180590,-0.038587,0.152847
0.250000,0.181962,-0.021914,0.204805
0.300000,0.179389,-0.019056,0.216333
0.350000,0.179046,-0.001715,0.211675
0.400000,0.179389,0.009814,0.086332

Currently it uses a system of 3 trials per a file
Currently its very static and not flexible in order to change the amount of trial find and replace 3 with the number of trials you choose
To change the number of expirements you did find and replace the number 5 with whatever number
To change the diffrence in mass each time I.E
3 trials of 10g then 3 trials of 20g the change is 10g find and replace 10 with whatever
The naming format MUST be as follows <WEIGHT>gt<TRIALNUMBER> then at the top of the file you must change add file names based on what you want so like using that format but list up at the top of the file BUT IT MUST BE GROUPED WITH THE TRIALS OF THE SAME EXPIREMENT
Values of the spoofer function have been <REDACTED> please set your own this determines the uniformity of curve.
  
spoofer settings that arent terrible are the following 
1.150000,0.283318,0.378729,0.280752 <-- IMPLICT
1.200000,0.302698,0.390544,0.260585 <-- IMPLICT
1.250000,0.322248,0.404073,0.248199 <-- IMPLICT
1.300000,0.343000,0.418174,0.182669 <-- EXPLICT
