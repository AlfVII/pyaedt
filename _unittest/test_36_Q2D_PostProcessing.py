import os

# from _unittest.conftest import BasisTest
from _unittest.conftest import config

# from _unittest.conftest import local_path
import pytest

from pyaedt import Q2d

test_subfolder = "T36"

if config["desktopVersion"] > "2022.2":
    q2d_solved_sweep = "q2d_solved_sweep_231"
    q2d_solved_nominal = "q2d_solved_nominal_231"
else:
    q2d_solved_sweep = "q2d_solved_sweep"
    q2d_solved_nominal = "q2d_solved_nominal"


@pytest.fixture(scope="class")
def q2d_solved_sweep_app(add_app):
    app = add_app(application=Q2d, project_name=q2d_solved_sweep, subfolder=test_subfolder)
    return app


@pytest.fixture(scope="class")
def q2d_solved_nominal_app(add_app):
    app = add_app(application=Q2d, project_name=q2d_solved_nominal, subfolder=test_subfolder)
    return app


class TestClass:
    # def setup_class(self):
    #     BasisTest.my_setup(self)
    #
    # def teardown_class(self):
    #     BasisTest.my_teardown(self)

    @pytest.fixture(autouse=True)
    def init(self, q2d_solved_sweep_app, q2d_solved_nominal_app, local_scratch):
        self.q2d_solved_sweep_app = q2d_solved_sweep_app
        self.q2d_solved_nominal_app = q2d_solved_nominal_app
        self.local_scratch = local_scratch

    def test_01_export_w_elements_from_sweep(self, q2d_solved_sweep_app, local_scratch):
        # test_project = self.local_scratch.copyfile(
        #     os.path.join(local_path, "example_models", test_subfolder, q2d_solved_sweep + ".aedtz")
        # )
        # with Q2d(test_project, specified_version=config["desktopVersion"]) as q2d:
        #     try:
        #         export_folder = os.path.join(self.local_scratch.path, "export_folder")
        #         files = q2d.export_w_elements(False, export_folder)
        #         assert len(files) == 3
        #         for file in files:
        #             _, ext = os.path.splitext(file)
        #             assert ext == ".sp"
        #             assert os.path.isfile(file)
        #     finally:
        #         q2d.close_project(save_project=False)

        export_folder = os.path.join(local_scratch.path, "export_folder")
        files = q2d_solved_sweep_app.export_w_elements(False, export_folder)
        assert len(files) == 3
        for file in files:
            _, ext = os.path.splitext(file)
            assert ext == ".sp"
            assert os.path.isfile(file)

    def test_02_export_w_elements_from_nominal(self, q2d_solved_nominal_app, local_scratch):
        # test_project = self.local_scratch.copyfile(
        #     os.path.join(local_path, "example_models", test_subfolder, q2d_solved_nominal + ".aedtz")
        # )
        # with Q2d(test_project, specified_version=config["desktopVersion"]) as q2d:
        #     try:
        #         export_folder = os.path.join(self.local_scratch.path, "export_folder")
        #         files = q2d.export_w_elements(False, export_folder)
        #         assert len(files) == 1
        #         for file in files:
        #             _, ext = os.path.splitext(file)
        #             assert ext == ".sp"
        #             assert os.path.isfile(file)
        #     finally:
        #         q2d.close_project(save_project=False)

        export_folder = os.path.join(local_scratch.path, "export_folder")
        files = q2d_solved_nominal_app.export_w_elements(False, export_folder)
        assert len(files) == 1
        for file in files:
            _, ext = os.path.splitext(file)
            assert ext == ".sp"
            assert os.path.isfile(file)

    def test_03_export_w_elements_to_working_directory(self, q2d_solved_nominal_app):
        # test_project = self.local_scratch.copyfile(
        #     os.path.join(local_path, "example_models", test_subfolder, q2d_solved_nominal + ".aedtz")
        # )
        # with Q2d(test_project, specified_version=config["desktopVersion"]) as q2d:
        #     try:
        #         files = q2d.export_w_elements(False)
        #         assert len(files) == 1
        #         for file in files:
        #             _, ext = os.path.splitext(file)
        #             assert ext == ".sp"
        #             assert os.path.isfile(file)
        #             file_dir = os.path.abspath(os.path.dirname(file))
        #             assert file_dir == os.path.abspath(q2d.working_directory)
        #     finally:
        #         q2d.close_project(save_project=False)

        files = q2d_solved_nominal_app.export_w_elements(False)
        assert len(files) == 1
        for file in files:
            _, ext = os.path.splitext(file)
            assert ext == ".sp"
            assert os.path.isfile(file)
            file_dir = os.path.abspath(os.path.dirname(file))
            assert file_dir == os.path.abspath(self.q2d_solved_nominal_app.working_directory)
