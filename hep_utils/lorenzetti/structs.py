import ROOT

CPP_STRUCTS = "\
    namespace xAOD{\
        struct CaloCell_t{\
            float e;\
            float et;\
            float tau; \
            float eta;\
            float phi;\
            float deta;\
            float dphi;\
            int descriptor_link;\
        };\
        struct CaloDetDescriptor_t{\
            int sampling;\
            int detector;\
            float eta;\
            float phi;\
            float deta;\
            float dphi;\
            float e;\
            float tau;\
            float edep;\
            int bcid_start;\
            int bcid_end;\
            float bc_duration;\
            std::vector<float> pulse;\
            std::vector<float> edep_per_bunch;\
            std::vector<float> tof;\
            unsigned long int hash;\
            int cell_link;\
            float z;\
        };\
        struct CaloCluster_t{\
            float e;\
            float et;\
            float eta;\
            float phi;\
            float deta;\
            float dphi;\
            float e0;\
            float e1;\
            float e2;\
            float e3;\
            float ehad1;\
            float ehad2;\
            float ehad3;\
            float etot;\
            float e233;\
            float e237;\
            float e277;\
            float emaxs1;\
            float emaxs2;\
            float e2tsts1;\
            float reta;\
            float rphi;\
            float rhad;\
            float rhad1;\
            float eratio;\
            float f0;\
            float f1;\
            float f2;\
            float f3;\
            float weta2;\
            float secondR;\
            float lambdaCenter;\
            float secondLambda;\
            float fracMax;\
            float lateralMom;\
            float longitudinalMom;\
            std::vector<int> cell_links;\
        };\
        struct CaloRings_t{\
            int cluster_link;\
            std::vector<float> rings;\
        };\
        struct EventInfo_t{\
            float eventNumber;\
            float avgmu;\
        };\
        struct TruthParticle_t{\
            int pdgid;\
            int seedid;\
            float e;\
            float et;\
            float eta;\
            float phi;\
            float px;\
            float py;\
            float pz;\
            float vx;\
            float vy;\
            float vz;\
        };\
        struct Electron_t{\
            int cluster_link;\
            float e;\
            float et;\
            float eta;\
            float phi;\
            std::vector<bool> decisions;\
        };\
        struct EventSeed_t{\
            int id;\
            float e;\
            float et;\
            float eta;\
            float phi;\
            };\
    }"


def declare():
    """
    Declare the lorenzetti structs in ROOT
    """
    ROOT.gROOT.ProcessLine(CPP_STRUCTS)