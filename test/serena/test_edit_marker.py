from serena.tools import ListDirTool, ReplaceRegexTool, Tool


class TestEditMarker:
    def test_tool_can_edit_method(self):
        """Test that Tool.can_edit() method works correctly"""
        # Non-editing tool should return False
        assert issubclass(ListDirTool, Tool)
        assert not ListDirTool.can_edit()

        # Editing tool should return True
        assert issubclass(ReplaceRegexTool, Tool)
        assert ReplaceRegexTool.can_edit()
