import os
import sys
import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditingLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary


def main():
    # 获取所选材质
    # selected_material = unreal.EdGraphPinType.get_editor_property("DefaultObject")
    # file_path = unreal.EdGraphPinType.get_editor_property("DefaultObject")
    # file_name = unreal.EdGraphPinType.get_editor_property("DefaultObject")
    if not selected_material:
        print('Failed to get material instance')
        return
    print(f'{selected_material}')

    # mi_path = "/Game/Tools"
    mi_asset = AssetTools.create_asset(file_name, file_path, unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
    # set material instance parameters!
    MaterialEditingLibrary.set_material_instance_parent(mi_asset, selected_material)  # set parent material
    # MaterialEditingLibrary.set_material_instance_scalar_parameter_value(mi_asset, "Desaturation", 0.3)  # set scalar parameter
    EditorAssetLibrary.save_loaded_asset(mi_asset)
    return 0


if __name__ == '__main__':
    sys.exit(main())
