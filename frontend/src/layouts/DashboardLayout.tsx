import AppSidebar from "@/components/dashboard/sidebar/AppSidebar";
import AppTopbar from "@/components/dashboard/sidebar/topbar/AppTopbar";
import ReactQueryProvider from "@/components/providers/ReactQueryProvider";
import { Outlet } from "react-router-dom";

const DashboardLayout = () => {
    return (
        <div className="w-full">
            <ReactQueryProvider>
                <AppTopbar />
                <div className="flex">
                    <AppSidebar />
                    <div className="w-full ml-2 h-[90vh] overflow-hidden">
                        <Outlet />
                    </div>
                </div>
            </ReactQueryProvider>
        </div>
    )
}

export default DashboardLayout