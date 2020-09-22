# Biases in, and corrections to, KSB shear measurements. Viola et al, 2010
Notes and tools derived from reading groups sessions

[arxiv link](https://arxiv.org/abs/1006.2470)

## Goals of the Paper

1. Show the theoretical and practical caveats of KSB.
2. Suggest an amelioration of KSB.

## Main Results and Conclusion

1. The assumptions in KSB introduce biaises especially for large amplitude
values.
2. Rewriting correctly the Taylor expansion of the ellipticity up to the third
order (see KSB3) gives results with biaises smaller by orders of magnitude.
3. The PSF corrections in KSB are not accurate however they partially cancel
other biaises.

## Definitions and Equations

*. Reduced shear, g: (eq. 7)
*. Complex ellipticity, $\chi$: (eq. 10)
*. Shear responsivity $\epsilon$: (eq. 14)
*. KSB (eq. 32)
*. KSB1 (eq. 34)
*. KSBtr (eq.36)
*. KSB3 (eq. 44)
*. Inverse Problem (eq. 50)
*. Circular PSF Formula (eq. 58)
*. Anisotropic PSf Formula (eq. 67)

> The reduced shear, g, is preferred over the shear responsivity,
$\epsilon$, for its robustness to noise in the data.

## Assumptions in KSB
1. The reduced shear, g, is constant and the ellipticity average is null,
$\left< \chi \right>=0$ (see eq. 12).
2. Many Taylor expansions like in the reduced shear, g (see eq. 29).
> Taylor expansions gives a polynomial approximation around a certain reference
value. The further from the reference we evaluate the expansion the bigger the
biais. In this paper, since the reference value is zero, the biais will be
greater for large amplitude values.

3. Assume equality between (eq. 27) and (eq. 28).
4. The PSF has at most slight anisotropies, it is mostly circular.

## Notations Clarification

1. The angular coordinates are solid angles so they have two components. These
coordinates can be assimilated to linear coordinates.
2. The star in eq. 12 stands for the conjugate.
3. Rewriting eq.48-50:
  i. (eq. 48) $$\chi = f\left( \tilde{g}, \chi^{s}\right)$$
  ii. (eq. 49) $$\chi = h \left( \chi^{obs}\right)$$
  iii. (eq. 50) $$\chi^{obs} = h^{-1}\left[ f \left( \tilde{g}, h\left(\chi^{obs}\right)\right)\right]$$

  where $\chi^{s}$ is the intrinsic ellipticity of the galaxy, $\chi^{obs}$ is
  the ellipticity of the lensed galaxy and $\chi$ is the ellipticity of the
  convoluted and lensed galaxy.
4. In (eq. 51): $$\chi^{sh}_{\alpha} = \chi_{\alpha} + \chi^{s}_{\alpha}$$
5. In (eq. 52): the asterisk, *, in $P^{sm,*}$ is to indicate the PSF.
Explanation: * --> star --> dirac --> PSF --> illuminati

## Implementation

[Link](https://github.com/pmelchior/shapelens/blob/master/src/KSB.cc) to Peter Melchior implementation of KSB codes in C.
