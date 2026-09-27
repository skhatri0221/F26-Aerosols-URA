run10Up:
	( cp -r Template 0_3Lam_10)
	( cp transportProperties_10 0_3Lam_10/scalarTransport/constant/transportProperties)
	( cd 0_3Lam_10 && make runScalar)
	( cp 0_3Lam_10/scalarTransport/postProcessing/OutletFlowRate/0/surfaceFieldValue.dat 0_3Lam_10Up_phi.dat)
	( cp 0_3Lam_10/scalarTransport/postProcessing/OutletFlowRateT/0/surfaceFieldValue.dat 0_3Lam_10Up_phiT.dat)
run25Up:
	( cp -r Template 0_3Lam_25)
	( cp transportProperties_25 0_3Lam_25/scalarTransport/constant/transportProperties)
	( cd 0_3Lam_25 && make runScalar)
	( cp 0_3Lam_25/scalarTransport/postProcessing/OutletFlowRate/0/surfaceFieldValue.dat 0_3Lam_25Up_phi.dat)
	( cp 0_3Lam_25/scalarTransport/postProcessing/OutletFlowRateT/0/surfaceFieldValue.dat 0_3Lam_25Up_phiT.dat)
run50Up:
	( cp -r Template 0_3Lam_50)
	( cp transportProperties_50 0_3Lam_50/scalarTransport/constant/transportProperties)
	( cd 0_3Lam_50 && make runScalar)
	( cp 0_3Lam_50/scalarTransport/postProcessing/OutletFlowRate/0/surfaceFieldValue.dat 0_3Lam_50Up_phi.dat)
	( cp 0_3Lam_50/scalarTransport/postProcessing/OutletFlowRateT/0/surfaceFieldValue.dat 0_3Lam_50Up_phiT.dat)
run100Up:
	( cp -r Template 0_3Lam_100)
	( cp transportProperties_100 0_3Lam_100/scalarTransport/constant/transportProperties)
	( cd 0_3Lam_100 && make runScalar)
	( cp 0_3Lam_100/scalarTransport/postProcessing/OutletFlowRate/0/surfaceFieldValue.dat 0_3Lam_100Up_phi.dat)
	( cp 0_3Lam_100/scalarTransport/postProcessing/OutletFlowRateT/0/surfaceFieldValue.dat 0_3Lam_100Up_phiT.dat)
run200Up:
	( cp -r Template 0_3Lam_200)
	( cp transportProperties_200 0_3Lam_200/scalarTransport/constant/transportProperties)
	( cd 0_3Lam_200 && make runScalar)
	( cp 0_3Lam_200/scalarTransport/postProcessing/OutletFlowRate/0/surfaceFieldValue.dat 0_3Lam_200Up_phi.dat)
	( cp 0_3Lam_200/scalarTransport/postProcessing/OutletFlowRateT/0/surfaceFieldValue.dat 0_3Lam_200Up_phiT.dat)
run225Up:
	( cp -r Template 0_3Lam_225)
	( cp transportProperties_225 0_3Lam_225/scalarTransport/constant/transportProperties)
	( cd 0_3Lam_225 && make runScalar)
	( cp 0_3Lam_225/scalarTransport/postProcessing/OutletFlowRate/0/surfaceFieldValue.dat 0_3Lam_225Up_phi.dat)
	( cp 0_3Lam_225/scalarTransport/postProcessing/OutletFlowRateT/0/surfaceFieldValue.dat 0_3Lam_225Up_phiT.dat)
run300Up:
	( cp -r Template 0_3Lam_300)
	( cp transportProperties_300 0_3Lam_300/scalarTransport/constant/transportProperties)
	( cd 0_3Lam_300 && make runScalar)
	( cp 0_3Lam_300/scalarTransport/postProcessing/OutletFlowRate/0/surfaceFieldValue.dat 0_3Lam_300Up_phi.dat)
	( cp 0_3Lam_300/scalarTransport/postProcessing/OutletFlowRateT/0/surfaceFieldValue.dat 0_3Lam_300Up_phiT.dat)
run225Down:
	( cp controlDict 0_3Lam_225/scalarTransport/system/)
	( cd 0_3Lam_225 && make runScalar)
	( cp 0_3Lam_225/scalarTransport/postProcessing/OutletFlowRate/1000/surfaceFieldValue.dat 0_3Lam_225Down_phi.dat)
	( cp 0_3Lam_225/scalarTransport/postProcessing/OutletFlowRateT/1000/surfaceFieldValue.dat 0_3Lam_225Down_phiT.dat)
runAllUp:
	( make run10Up)
	( make run25Up)
	( make run50Up)
	( make run100Up)
	( make run200Up)
	( make run300Up)
runAllDown:
	( make run225Down)
removeDir:
	( rm -rf 0_3*)
	( rm *.dat)
###############