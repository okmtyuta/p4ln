import os

import torch

from src.modules.extract.language.quick_esm.quick_esm1b import QuickESM1bLanguage
from src.modules.extract.language.quick_esm.quick_esm2 import QuickESM2Language
from src.lib.config.dir import Dir
from src.modules.extract.language.esm.esm1b import ESM1bLanguage
from src.modules.extract.language.esm.esm2 import ESM2Language
from src.modules.extract.language.esm.esm_converter import ESMConverter
from src.modules.protein.protein_list import ProteinList


class TestQuickESMLanguage:
    def test_quick_esm2_language(self):
        path = os.path.join(Dir.test_sources_dir, "data.csv")
        protein_list = ProteinList.from_csv(path)

        quick_esm2_language = QuickESM2Language()

        protein_list = quick_esm2_language(protein_list=protein_list)

        esm2_converter = ESMConverter("esm2")
        for protein in protein_list.proteins:
            assert torch.equal(protein.representations, esm2_converter(list(protein.seq)))

    def test_quick_esm1b_language(self):
        path = os.path.join(Dir.test_sources_dir, "data.csv")
        protein_list = ProteinList.from_csv(path)

        quick_esm1b_language = QuickESM1bLanguage()

        protein_list = quick_esm1b_language(protein_list=protein_list)

        esm1b_converter = ESMConverter("esm1b")
        for protein in protein_list.proteins:
            assert torch.equal(protein.representations, esm1b_converter(list(protein.seq)))
