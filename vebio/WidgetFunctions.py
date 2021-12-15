from ipywidgets import *

from vebio.Utilities import dict_to_yaml, yaml_to_dict

#================================================================

class WidgetCollection:
    """A ``WidgetCollection`` object collects any number of different iPyWidgets.

    This object can be used to organize all the widgets pertaining to a single
    unit model or step of the overall conversion process.  New widgets should be
    accumulated after initialization using an approach like::


        fs_options = wf.WidgetCollection()
        fs_options.xylan_solid_fraction = widgets.BoundedFloatText(...)
        fs_options.glucan_solid_fraction = widgets.BoundedFloatText(...)
        fs_options.initial_porosity = widgets.Checkbox(...)

    where widget options and values can be accessed using, for example,
    ``fs_options.initial_porosity.value``

    """
    def __init__(self):

        pass

    def display_all_widgets(self):
        """Displays all the collected widgets in the Notebook.

        This method displays all the widgets collected in the object
        to the Jupyter Notebook interface.

        Args:
            None

        Returns:
            None

        """
        
        pass

    def export_widgets_to_dict(self, parent_name=None):
        """Store all widget values in dictionary.

        This method allows the values of each widget to be saved
        in a dictionary with the pattern ``{"widget_1_name": widget_1_value, ...}``.
        If the widget was created with a scaling function, the scaled
        version of the value is calculated and stored in the dictionary.
        This scaled value is the one that will be referenced by subsequent operations
        accessing the VE parameter file.

        Args:
            parent_name (str, optional):
                At the end of the dictionary creation, all the ``name: value``
                entries can be nested under a single "parent" keyword.  For example::

                    {parent_name: {"widget_1_name": widget_1_value,
                                   "widget_2_name": widget_2_value}}

                Defaults to ``None``, i.e., do not nest under a parent name.

        Returns:
            dict:
                The name and value of each widget
                collected in a Python dictionary.
            
        """

        pass

#================================================================

class ValueRangeWidget:
    """A pair of linked ``BoundedFloatText`` widgets for value ranges.

    This is a custom widget composed of two linked ``BoundedFloatText`` widgets
    intended to enable the easy solicitation of a range of values from the user.

        
    """

    def __init__(self, description, tooltip, bounds, init_vals, step_size):

        """Initialize the linked input fields.

        These linked widgets will be displayed side-by-side for intuitive
        entry of [lower_bound, upper_bound] information, the behavior of the
        individual fields and their labeling/description is provided by the user.

        Args:
            description (string):
                A short name or label for the the widget, e.g., `Porosity Range`
            tooltip (string):
                A longer, potentially multi-line explanation describing the 
                values that are intended to be entered, background information,
                units, suggested values, etc., should all be communicated here.
            bounds (list(float)):
                A two-element list where ``bounds[0]`` is the lower bound to enforce
                on both fields and ``bounds[1]`` is the upper bound to enforce on
                both fields.
            init_vals (list(float)):
                A two-element list where ``init_vals[0]`` is the initial value of the
                lower bound and ``init_vals[1]`` is the initial value of the upper bound.
            step_size (float):
                The change in value produced by clicking the increment or decrement
                buttons in the ``BoundedFloatText`` field.

        Returns:
            None

        """

        pass
        