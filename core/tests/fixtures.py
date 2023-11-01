import pytest

from core.parallel import MpiConfig
from core.config import ConfigOptions
from core.geoMod import GeoMetaWrfHydro

import numpy as np


@pytest.fixture
def mpi_meta(config_options):
    config_options.read_config()

    mpi_meta = MpiConfig()
    mpi_meta.initialize_comm(config_options)

    return mpi_meta

@pytest.fixture
def geo_meta(config_options, mpi_meta):
    config_options.read_config()

    WrfHydroGeoMeta = GeoMetaWrfHydro()
    WrfHydroGeoMeta.initialize_destination_geo(config_options, mpi_meta)
    WrfHydroGeoMeta.initialize_geospatial_metadata(config_options, mpi_meta)

    return WrfHydroGeoMeta

@pytest.fixture
def config_options():
    config_path = './yaml/configOptions_valid.yaml'
    config_options = ConfigOptions(config_path)
    config_options.read_config()
    yield config_options

@pytest.fixture
def config_options_cfs():
    config_path = './yaml/configOptions_cfs.yaml'
    config_options = ConfigOptions(config_path)
    config_options.read_config()
    yield config_options

