import numpy as np
import plotly.graph_objects as go

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

# Plot the intensity profile using Plotly
fig = go.Figure()

fig.add_trace(go.Heatmap(
    z=intensity,
    x=z,
    y=r,
    colorscale='Inferno',
    colorbar=dict(title='Intensity')
))

fig.update_layout(
    title='Gaussian Beam Side View with Envelope Line',
    xaxis_title='Propagation distance z (m)',
    yaxis_title='Radial distance r (m)',
    yaxis=dict(scaleanchor="x", scaleratio=1)
)

fig.show()
