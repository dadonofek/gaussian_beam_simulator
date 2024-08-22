import numpy as np
import matplotlib.pyplot as plt

# Define parameters
wavelength = 500e-9  # Wavelength in meters (e.g., 500 nm)
w0 = 1e-3  # Beam waist in meters (e.g., 1 mm)
z_R = np.pi * w0**2 / wavelength  # Rayleigh range

# Create a grid of points in z (propagation direction) and r (radial direction)
z = np.linspace(-2*z_R, 2*z_R, 500)
r = np.linspace(-3*w0, 3*w0, 500)
Z, R = np.meshgrid(z, r)

# Calculate the beam width at each z
w_z = w0 * np.sqrt(1 + (Z / z_R)**2)

# Calculate intensity profile as a function of z and r
intensity = (w0 / w_z)**2 * np.exp(-2 * R**2 / w_z**2)

# Plot the intensity profile
plt.figure(figsize=(10, 6))
plt.imshow(intensity, extent=[-2*z_R, 2*z_R, -3*w0, 3*w0], origin='lower', aspect='auto', cmap='inferno')
plt.colorbar(label='Intensity')
plt.title('Gaussian Beam Side View with Envelope Line')
plt.xlabel('Propagation distance z (m)')
plt.ylabel('Radial distance r (m)')

# Plot the envelope line where the intensity drops to 1/e^2 of the maximum
envelope_r = w0 * np.sqrt(1 + (z / z_R)**2)
plt.plot(z, envelope_r, color='cyan', linestyle='--', label=r'$r(z) = w(z)$ (Envelope)')
plt.plot(z, -envelope_r, color='cyan', linestyle='--')

# Mark the beam waist and Rayleigh range
plt.axvline(x=0, color='white', linestyle='--', label='Beam Waist (z=0)')
plt.axvline(x=z_R, color='white', linestyle='--', label='Rayleigh Range (z=z_R)')
plt.axvline(x=-z_R, color='white', linestyle='--')

plt.legend()

plt.show()
