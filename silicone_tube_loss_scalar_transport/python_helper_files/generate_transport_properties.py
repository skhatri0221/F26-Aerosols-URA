
particle_sizes_nm = [10, 25, 50, 100, 200, 300]

diffusion_coefficients = [
    5.43e-8,
    9.01e-9,
    2.40e-9,
    6.86e-10,
    2.21e-10,
    1.23e-10
]

if len(particle_sizes_nm) != len(diffusion_coefficients):
    raise ValueError("Particle size list and diffusion coefficient list must have the same length.")

header = """/*--------------------------------*- C++ -*----------------------------------*\\
  =========                 |
  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\\\    /   O peration     | Website:  https://openfoam.org
    \\\\  /    A nd           | Version:  9
     \\\\/     M anipulation  |
\\*---------------------------------------------------------------------------*/
FoamFile
{
    format      ascii;
    class       dictionary;
    location    "constant";
    object      transportProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

"""

footer = """
// ************************************************************************* //
"""

for size, diffusion in zip(particle_sizes_nm, diffusion_coefficients):

    filename = f"transportProperties_{size}"

    content = (
        header
        + f"D              D [0 2 -1 0 0 0 0] {diffusion};\n"
        + "ScT            ScT [0 0 0 0 0 0 0] 0.7;\n"
        + footer
    )

    with open(filename, "w") as file:
        file.write(content)

    print(f"Created {filename}")