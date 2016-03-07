from base import BaseObject, dynamicProperty

class BaseSegment(BaseObject):

    # --------------
    # Identification
    # --------------

    index = dynamicProperty("index", "The index of the segment within the ordered list of the parent contour's segments. None if the segment does not belong to a contour.")

    def _get_index(self):
        self.raiseNotImplementedError()

    # ----------
    # Attributes
    # ----------

    type = dynamicProperty("type", "The segment type. The possible types are move, line, curve, qcurve.")

    def _get_type(self):
        pass

    def _set_type(self, value):
        pass

    smooth = dynamicProperty("smooth", "Boolean indicating if the segment is smooth or not.")

    def _get_smooth(self):
        pass

    def _set_smooth(self, value):
        pass

    # ------
    # Points
    # ------

    def __getitem__(self, index):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    points = dynamicProperty("points", "A list of points in the segment.")

    def _get_points(self):
        self.raiseNotImplementedError()

    onCurve = dynamicProperty("onCurve", "The on curve point in the segment.")

    def _get_onCurve(self):
        pass

    offCurve = dynamicProperty("offCurve", "The off curve points in the segment.")

    def _get_offCurve(self):
        pass

    def insertPoint(self, index, pointType, point):
        """
        Insert a point into the segment.
        """
        pass

    def removePoint(self, index):
        """
        Remove a point from the segment.
        """
        pass

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix):
        """
        Transform the segment with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """

    def move(self, value):
        """
        Move the segment by value. Value must
        be a tuple defining x and y values.
        """

    def scale(self, value, center=None):
        """
        Scale the segment by value. Value must be a
        tuple defining x and y values.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None):
        """
        Rotate the segment by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """

    def skew(self, angle, offset=None):
        """
        Skew the segment by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the skew.
        """

    # ----
    # Misc
    # ----

    def round(self):
        """
        Round coordinates in all points.
        """

    def copy(self):
        """
        Copy this segment by duplicating the data into
        a segment that does not belong to a contour.
        """
