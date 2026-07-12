import AppContainer from "./AppContainer.js";
import Sidebar from "./Sidebar.js";
import Topbar from "./Topbar.js";
import Content from "./Content.js";

const DashboardShell = ({
    title = "Dashboard",
    activeMenu = "dashboard",
    user = {},
    children = ""
} = {}) => {

    return AppContainer({

        sidebar: Sidebar(activeMenu),

        topbar: Topbar({
            title,
            user
        }),

        children: Content({
            children
        })

    });

};

export default DashboardShell;