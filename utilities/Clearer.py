from Entities.Bodega import Bodega
from Entities.Pais import Pais
from Entities.Provincia import Provincia
from Entities.RegionVitivinicola import RegionVitivinicola
from Entities.Varietal import Varietal
from Entities.Vino import Vino

class Clearer:
    @staticmethod
    def limpiar_todas_las_instancias():
        Vino.limpiar_instancias()
        Bodega.limpiar_instancias()
        Pais.limpiar_instancias()
        Provincia.limpiar_instancias()
        RegionVitivinicola.limpiar_instancias()
        Varietal.limpiar_instancias()
