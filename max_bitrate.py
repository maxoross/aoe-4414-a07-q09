# max_bitrate.py

# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# Description: Outputs the maximum achievable bitrate for a transmission

# Parameters:
#tx_w: Transmitter power in watts
#tx_gain_db: Transmitter antenna gain in dB
#freq_hz: Frequency in Hz
#dist_km: Distance between the transmitter and receiver in km
#rx_gain_db: Receiver antenna gain in dB
#n0_j: Noise spectral density in J
#bw_hz: Bandwidth in Hz

# Output:
#  The maximum achievable bitrate for a transmission

# Written by Maxwell Oross
# Other contributors: None

# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math
import sys

#Constants 
c = 2.99792458e8  # Speed of light in m/s
L_l = 10**(-1/10)  # Transmitter to antenna line loss (dB)
L_atm = 10**(0/10)  # Atmospheric loss (dB)

# initialize script arguments
tx_w = float(sys.argv[1])
tx_gain_db = float(sys.argv[2])
freq_hz = float(sys.argv[3])
dist_km = float(sys.argv[4])
rx_gain_db = float(sys.argv[5])
n0_j = float(sys.argv[6])
bw_hz = float(sys.argv[7])

# parse script arguments
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
  print(\
   'Usage: '\
   'python3 pool_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()

#Correcting Units
dist_m = dist_km * 1000  # Distance in meters
lam = c / freq_hz  # Wavelength in meters
G_t=10**(tx_gain_db/10) 
G_r=10**(rx_gain_db/10)

# Calc Recieved Signal Power
C = tx_w * L_l * G_t * (lam/(4*math.pi*dist_m))**2 *L_atm * G_r

#Calc Recieved Noise Power
N = n0_j*bw_hz

#Calc Max Achievable Bitrate
r_max = bw_hz*math.log((1+(C/N)),2)

# Display final answers
print(math.floor(r_max)) #outputs the maximum achievable bitrate
